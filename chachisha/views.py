from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(req) :
    return render (req, 'index.html')

# @TODO:get all posts 
def home(req):
    data = {
        'posts' : Post.objects.all()
    }

    return render(req,'home.html',data)

# @TODO:get user credentials 
def profile(req):

    return render(req,'profile.html')
