from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import datetime


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=False,
            is_active=True,
            is_superuser=False,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            is_staff=True,
            is_active=True,
            is_superuser=True,
            last_login=now,
            date_joined=now,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    states = (
              ('AndhraPradesh', 'Andhra Pradesh'),
              ('ArunachalPradesh', 'Arunachal Pradesh'),
              ('Assam', 'Assam'),
              ('Sikkim', 'Sikkim'),
              ('Nagaland', 'Nagaland'),
              ('Manipur', 'Manipur'),
              ('Meghalaya', 'Meghalaya'),
              ('Jammukashmir', 'Jammu kashmir'),
              ('Punjab', 'Punjab'),
              ('Himachalpradesh', 'Himachal pradesh'),
              ('Haryana', 'Haryana'),
              ('Uttarakhand', 'Uttarakhand'),
              ('Uttarpradesh', 'Uttar pradesh'),
              ('Rajasthan', 'Rajasthan'),
              ('Gujarat', 'Gujarat'),
              ('MadhyaPradesh', 'Madhya Pradesh'),
              ('Jharkhand', 'Jharkhand'),
              ('WestBengal', 'West Bengal'),
              ('Maharastra', 'Maharastra'),
              ('Orissa', 'Orissa'),
              ('Chattisgarh', 'Chattisgarh'),
              ('Karnataka', 'Karnataka'),
              ('Kerala', 'Kerala'),
              ('TamilNadu', 'Tamil Nadu'),
              ('Mizoram', 'Mizoram'),
              ('Tripura', 'Tripura'),
              ('Goa', 'Goa'),
              ('Telangana', 'Telangana'),
              )
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True)

    is_doctor = models.BooleanField(default=False, null=True)
    is_patient = models.BooleanField(default=False, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    pin = models.PositiveIntegerField(null=True)
    state = models.CharField(max_length=25, null=True, choices=states)

    phone_regex = RegexValidator(regex=r'\d{4}-\d{7}|\d{10,15}',
                                 message="Phone number must be entered in the format: '0123456789 or 0123-1234567'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def doc_email(self):
        return self.email


class ExtendedDoctorsDetail(models.Model):
    specializations = (('dermatologist', 'dermatologist'),
                       ('General Physician', 'General Physician'),
                       ('gastroentrologist', 'gastroentrologist'),
                       ('Allergy & Immunologist', 'Allergy & Immunologist'),
                       ('Anesthesiologist', 'Anesthesiologist'),
                       ('Emergency Physicians', 'Emergency Physicians'),
                       ('Internist Physicians', 'Internist Physicians'),
                       ('Neurologist', 'Neurologist'),
                       ('gynaecologist', 'gynaecologist'),
                       ('opthalmologist', 'opthalmologist'),
                       ('pediatrician', 'pediatrician'),
                       ('psychiatrist', 'psychiatrist'),
                       ('urologist', 'urologist'),
                       ('cardiologist', 'cardiologist'),
                       ('orthopedecian', 'orthopedecian'),
                       ('Ortho Surgeon', 'Ortho Surgeon'),
                       ('Family Physician', 'Family Physician'),
                       ('Trauma surgeon', 'Trauma surgeon'),
                       ('Homeopathy', 'Homeopathy'),
                       ('pulmonologist', 'pulmonologist'),
                       ('cosmetic surgeon', 'cosmetic surgeon'),
                       ('Surgeon', 'Surgeon'),
                       ('dental', 'dental'),
                       ('radiologist', 'radiologist')
                       )

    doctor = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_detail', primary_key=True)
    specialization = models.CharField(max_length=50, null=True, choices=specializations)
    is_verified = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.doctor.email


class ExtendedPatientsDetail(models.Model):
    gender = (('Male', 'Male'),
              ('Female', 'Female'),
              ('Other', 'Other'))
    patient = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_detail', primary_key=True)
    age = models.IntegerField(null=True, validators=[MaxValueValidator(120), MinValueValidator(1)])
    gender = models.CharField(max_length=20, choices=gender, null=True)

    def __str__(self):
        return self.patient.email


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.is_doctor:
        ExtendedDoctorsDetail.objects.create(doctor=instance)
    elif created and instance.is_patient:
        ExtendedPatientsDetail.objects.create(patient=instance)

