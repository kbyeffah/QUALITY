from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy



def index(request):
    return render(request, 'index.html')

def pc(request):
    return render(request, 'pc.html')

def phone(request):
    return render(request, 'phone.html')

