from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required


def index(req) :
    return render (req, 'index.html')

# @TODO:get all posts 
@login_required
def home(req):
    data = {
        'posts' : Post.objects.all()
    }

    return render(req,'home.html',data)
