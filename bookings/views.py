
from django.shortcuts import render, redirect
from django.contrib import messages
from users.models import ExtendedDoctorsDetail, User
from .dates import today_day as today_date

from .models import *
from users.decorators import patient_required, doctor_required
from .dates import time_list
from .forms import ChangeStatusForm


@patient_required()
def bookingView(request):
    specialist_list = list(ExtendedDoctorsDetail.objects.values_list('specialization', flat=True).distinct())
    cities_list = list(User.objects.filter(is_doctor=True).values_list('city', flat=True).distinct())
    if request.method == 'POST' and 'search_doctors' in request.POST:
        specialist = request.POST['specialist']
        city = request.POST['city']
        doctors_extd = ExtendedDoctorsDetail.objects.filter(specialization=specialist,
                                                            doctor__city__icontains=city).values('doctor',
                                                                                                 'specialization')
        doctors_base = User.objects.filter(doctor_detail__specialization=specialist,
                                           city__icontains=city).values('id', 'email', 'name',
                                                                        'address', 'city',
                                                                        'pin', 'state')
        for doctor_e in doctors_extd:
            for doctor_b in doctors_base:
                if doctor_e['doctor'] == doctor_b['id']:
                    doctor_b.update(doctor_e)
        filtered_results = doctors_base
        return render(request, 'bookings.html',
                      {'spcs': specialist_list, 'cities': cities_list, 'doctors': filtered_results,
                       'time_slots': time_list()})
    elif request.method == 'POST' and 'confirm-booking-button' in request.POST:
        date = request.POST.get('selected_date')
        time = request.POST.get('selected_time')
        print(date, time)
        booked_doctor_mail = request.POST.get('confirm-booking-button')
        doctors_extd = ExtendedDoctorsDetail.objects.filter(doctor__email=booked_doctor_mail).values('doctor',
                                                                                                     'specialization')
        doctors_base = User.objects.filter(email=booked_doctor_mail).values('id', 'name',
                                                                            'address', 'city')
        doctors_extd = doctors_extd[0]
        doctors_base = doctors_base[0]
        if Booking.objects.filter(doctor_email__icontains=booked_doctor_mail, booked_date__icontains=date, booked_time__icontains=time).count() < 1:
            book = Booking()
            book.p_id = request.user.id
            book.patient_name = request.user.name
            book.patient_email = request.user.email
            book.patient_age = request.user.patient_detail.age
            book.d_id = doctors_extd['doctor']
            book.doctor_name = doctors_base['name']
            book.doctor_email = booked_doctor_mail
            book.city = doctors_base['city']
            book.specialization = doctors_extd['specialization']
            book.booked_date = date
            book.booked_time = time
            book.save()
            messages.success(request,
                             'Successfully Booked Appointment. For date ' + date + ' with Doctor ' + doctors_base[
                                 'name'])
            return redirect('bookings:show_appointment_patient')
        else:
            messages.error(request, 'Time slot '+time+' is is not available, for Dr. '+doctors_base["name"]+', Please select another slot !!')
    context = {
        'spcs': specialist_list,
        'cities': cities_list,
    }
    return render(request, 'bookings.html', context)


@patient_required()
def ShowAppointmentsPatients(request):
    u_email = request.user.email
    bookings = Booking.objects.filter(patient_email=u_email).values().order_by('booked_date')
    return render(request, 'show_bookings_patient.html', {'bookings': bookings, 'today': today_date})


@doctor_required()
def ShowAppointmentsDoctors(request):
    u_email = request.user.email
    bookings = Booking.objects.filter(doctor_email=u_email).values().order_by('booked_date')
    return render(request, 'show_appointment_doctor.html', {'bookings': bookings, 'today': today_date, 'change_status_form': ChangeStatusForm})


@doctor_required()
def ModifyAppointmentDoctors(request, pk):
    booking = Booking.objects.get(id=pk)
    modify_form = ChangeStatusForm(instance=booking)
    if request.method == 'POST':
        modify_appointment_form = ChangeStatusForm(request.POST, instance=booking)
        if modify_appointment_form.is_valid():
            modify_appointment_form.save()
        return redirect('bookings:show_appointment_doctor')
    return render(request, 'modify_bookings.html', {'modify_form': modify_form})


@patient_required()
def DeleteAppointmentView(request, pk):
    try:
        Booking.objects.filter(id=pk).delete()
    except Booking.DoesNotExist:
        pass

    u_email = request.user.email
    bookings = Booking.objects.filter(patient_email=u_email).values().order_by('booked_date')
    return render(request, 'show_bookings_patient.html', {'bookings': bookings, 'today': today_date})