import numpy as np
import pandas as pd
from django.contrib import messages
from sklearn.naive_bayes import GaussianNB
from .models import DatabaseFiles


# input_array
def GenerateMLModel(user_symptom_list):
    # get all the item from DiseaseDatabaseModel
    ddb_obj = DatabaseFiles.objects.all()
    if ddb_obj.filter(File_Type='TestingFile') and ddb_obj.filter(File_Type='TrainingFile'):
        train_obj = ddb_obj.filter(File_Type='TrainingFile').values('File_Path')
        test_obj = ddb_obj.filter(File_Type='TestingFile').values('File_Path')

        train_file_path = str(train_obj[0]['File_Path'])
        test_file_path = str(test_obj[0]['File_Path'])

        # access by file reference
        train_file = open('disease_database/database_files/'+train_file_path)
        test_file = open('disease_database/database_files/'+test_file_path)

        train_result = pd.read_csv(train_file)
        test_result = pd.read_csv(test_file)

        Features_Train = train_result.drop(['prognosis'], axis=1).values
        Target_Train = train_result['prognosis'].values

        # get headings as numpy array
        Features_Headings = train_result.columns[:-1].tolist()

        for i in range(len(Features_Headings)):
            if Features_Headings[i] in user_symptom_list:
                Features_Headings[i] = 1
            else:
                Features_Headings[i] = 0
        # convert_1D list to 2D list because predict function only takes 2D numpy array
        Features_Headings_2D = [Features_Headings]
        # print(Features_Headings_2D)
        user_symptom_array = np.asarray(np.asarray(Features_Headings_2D))
        # print(type(Features_Headings), len(Features_Headings))
        ################################
        # build model
        gnb = GaussianNB()
        # Train model
        gnb.fit(Features_Train, Target_Train)
        ################################
        # all the diseases that model can predict(41)
        diseases = np.unique(Target_Train)
        disease_dict = DoPrediction(user_symptom_array, gnb, diseases)
        return disease_dict
    else:
        d = dict()
        return d


def DoPrediction(features_predict, gnb, diseases):
    # predicting with probability for each disease

    predicts = gnb.predict_proba(features_predict)

    # create dictionary with key as disease and probability as value {'disease': 0.5}
    # predict_proba gives nested array,
    # when single row of data provided, we have to access the internal array
    pred_dict = dict(zip(diseases, predicts[0]))
    # sort dictionary based on probability
    dicts = sorted(pred_dict.items(), key=lambda x: x[1], reverse=True)

    d = dict()
    # print only top 3 disease with probability higher than 0.30
    for i in range(3):
        if dicts[i][1] >= 0.2:
            print(dicts[i][0], ' --> Accuracy: ', round(dicts[i][1] * 100), '%')
            d[dicts[i][0]] = round(dicts[i][1] * 100)
    return d