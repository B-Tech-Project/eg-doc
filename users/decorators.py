from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def patient_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='users:login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_patient, login_url=login_url, redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def doctor_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='users:login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_doctor, login_url=login_url, redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator