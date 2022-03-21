from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(req):
    form = UserCreationForm()

    return render (req, 'register.html', {'form':form})

def login(req):
    return render (req, 'login.html')
