from django.contrib import admin
from .models import DatabaseFiles, Symptom, Diseases
# Register your models here.


class FileAdmin(admin.ModelAdmin):
    list_display = ('File_Type', 'File_Path')


class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('disease_name', 'preview', 'symptoms')


admin.site.register(DatabaseFiles, FileAdmin)
admin.site.register(Symptom)
admin.site.register(Diseases, DiseaseAdmin)


admin.site.site_header = "EDP&DA  Admin"