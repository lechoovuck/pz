from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'accounts/register.html')


def login(request):
    return HttpResponse('login')


# Create your views here.
