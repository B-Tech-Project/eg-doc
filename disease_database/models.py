from __future__ import unicode_literals
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
import csv
import io
from django.db import models


class DatabaseFiles(models.Model):
    file_types = (('TrainingFile', 'Training File'),
                  ('TestingFile', 'Testing File')
                  )
    File_Type = models.CharField(max_length=20, unique=True, choices=file_types, null=False)
    File_Path = models.FileField(upload_to='dataset/')


@receiver(signal=post_delete, sender=DatabaseFiles)
def delete_file(sender, instance, **kwargs):
    instance.File_Path.delete(False)


class Symptom(models.Model):
    symptom = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.symptom


# Every time new file is saved in Disease Database Model
@receiver(signal=post_save, sender=DatabaseFiles)
def access_symptoms_list_from_csv(sender, instance, **kwargs):
    file_name = instance.File_Path
    decoded_file = file_name.read().decode('utf-8')
    file_string = io.StringIO(decoded_file)
    reader = csv.reader(file_string)
    symptom_list = next(reader)
    for item in symptom_list:
        if item != 'prognosis':
            Symptom.objects.get_or_create(symptom=item)


class Diseases(models.Model):
    disease_name = models.CharField(max_length=20, null=True)
    preview = models.CharField(max_length=1000, null=True)
    symptoms = models.CharField(max_length=1000, null=True)
    prevention = models.CharField(max_length=1000, null=True)
    treatment = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.disease_name
