from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'title' : 'Post One', 
#         'author' : 'post_author',
#         'image_upload': 'Uploaded Images goes here!',
#         'content' : 'this content is for post one',
#         'date_posted' : '21st Jan 2018',
#     },
#     {
#         'title' : 'Post Two', 
#         'author' : 'post_author - 2',
#         'image_upload': 'Uploaded Images goes here!',
#         'content' : 'this content is for post two only',
#         'date_posted' : '30th Jan 2018',
#     }
# ]

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
