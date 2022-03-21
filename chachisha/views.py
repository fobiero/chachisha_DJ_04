from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req,'index.html')

def profile(req):
    return render(req,'profile.html')
