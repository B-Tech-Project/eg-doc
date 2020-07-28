from django.contrib import admin
from .models import Booking
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'patient_email', 'doctor_name', 'city', 'booked_date')


admin.site.register(Booking, BookingAdmin)