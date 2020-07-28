from django.shortcuts import render
from django.shortcuts import redirect


def home_redirect(request):
    return redirect('/accounts/login/')
