from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (LoginpageView, ProfileView, ProfileViewPK, DoctorSignupView, PatientSignupView,
                    PatientProfileUpdateView, DoctorProfileUpdateView, ChangePasswordView)

app_name = 'users'

urlpatterns = [
    path('login/', LoginpageView, name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),

    path('profile/', login_required(ProfileView, login_url='users:login'), name='profile'),
    path('profile/<int:pk>/', login_required(ProfileViewPK, login_url='users:login'), name='profile_with_pk'),
    # path('Dprofile', login_required(ProfileView), name='Dprofile'),

    path('doctor/registration/', DoctorSignupView, name='doctor_registration'),
    path('patient/registration/', PatientSignupView, name='patient_registration'),

    path('Patient/update/', login_required(PatientProfileUpdateView, login_url='users:login'), name='Pupdateprofile'),
    path('Doctor/update/', login_required(DoctorProfileUpdateView, login_url='users:login'), name='Dupdateprofile'),

    path('change_password/', login_required(ChangePasswordView, login_url='users:login'), name='ChangePassword'),
]