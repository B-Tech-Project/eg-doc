from django.contrib.auth.decorators import login_required
from django.urls import path, include
from .views import ShowAppointmentsDoctors, ShowAppointmentsPatients, bookingView, ModifyAppointmentDoctors, DeleteAppointmentView
app_name = 'bookings'

urlpatterns = [
    path('patient/', login_required(ShowAppointmentsPatients, login_url='users:login'), name='show_appointment_patient'),
    path('doctor/', login_required(ShowAppointmentsDoctors, login_url='users:login'), name='show_appointment_doctor'),
    path('', bookingView, name='conform_booking'),

    path('doctor/appointments/<str:pk>/', login_required(ModifyAppointmentDoctors, login_url='users:login'), name='modify_appointment_doctor'),
    path('patient/appointments/delete/<str:pk>/', login_required(DeleteAppointmentView, login_url='users:login'), name='delete_appointment'),
]