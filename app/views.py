from django.shortcuts import render
from django.urls import path


def home(request):
    return render(request, 'home.html')

def pre_home(request):
    return render(request, 'pre_home.html')
