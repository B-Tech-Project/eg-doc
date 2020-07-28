from .models import Booking
from django import forms


class AppointmentBookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['p_id', 'patient_name', 'patient_email', 'd_id', 'doctor_name', 'doctor_email', 'specialization', 'city', 'booked_date', 'booked_time']


class ChangeStatusForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['status', 'doctors_advice']