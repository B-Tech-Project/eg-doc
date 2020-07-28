from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User, ExtendedDoctorsDetail, ExtendedPatientsDetail


class UserSignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'password1', 'password2', 'name', 'address', 'city', 'pin', 'state')


class ExtendedDoctorsDetailForm(forms.ModelForm):
    # open_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'))
    # close_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'))
    class Meta:
        model = ExtendedDoctorsDetail
        fields = ('specialization',)


class ExtendedPatientsDetailForm(forms.ModelForm):
    class Meta:
        model = ExtendedPatientsDetail
        fields = ('age', 'gender')

# to update user profile


class UpdateUserProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ('name', 'phone_number', 'address', 'city', 'pin', 'state')


class UpdateDoctorProfile(forms.ModelForm):
    # open_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'))
    # close_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'))

    class Meta:
        model = ExtendedDoctorsDetail
        fields = ('specialization',)


class UpdatePatientProfile(forms.ModelForm):
    class Meta:
        model = ExtendedPatientsDetail
        fields = ('age', 'gender')