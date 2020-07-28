from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import SearchView, prediction_result_list_view, about_disease, covid19_view
app_name = 'disease_database'

urlpatterns = [
    path('prediction/', login_required(SearchView, login_url='users:login'), name='search'),
    path('prediction/submit/', login_required(prediction_result_list_view, login_url='users:login'), name='submit_symptom'),
    path('prediction/search/', login_required(about_disease, login_url='users:login'), name='disease_info'),

    path('covid-19/', covid19_view, name='covid19'),

]