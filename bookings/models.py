from django.db import models
from users.models import ExtendedDoctorsDetail, ExtendedPatientsDetail
# Create your models here.


class Booking(models.Model):
    status_options = (('Pending', 'Pending'),
                      ('Attended', 'Attended'))
    p_id = models.IntegerField(null=True)
    patient_name = models.CharField(max_length=30, null=True)
    patient_email = models.CharField(max_length=50, null=True)
    patient_age = models.CharField(max_length=2, null=True)

    d_id = models.IntegerField(null=True)
    doctor_name = models.CharField(max_length=30, null=True)
    doctor_email = models.CharField(max_length=50, null=True)
    specialization = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=100, null=True)

    booked_date = models.CharField(max_length=50, null=True)
    booked_time = models.CharField(max_length=50, null=True)

    doctors_advice = models.TextField(max_length=200, null=True, default='None')
    status = models.CharField(max_length=20, null=True, choices=status_options, default='Pending')

    '''def __str__(self):
        return self.patient_name'''