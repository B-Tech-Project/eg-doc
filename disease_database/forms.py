from django.forms import ModelForm
from .models import DatabaseFiles


class DiseaseSearchForm(ModelForm):
    class Meta:
        model = DatabaseFiles
        fields = ['File_Type', 'File_Path']
