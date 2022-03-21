from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title' : 'Post One', 
        'author' : 'post_author',
        'content' : 'this content is for post one',
        'date_posted' : '21st Jan 2018',
    },
    {
        'title' : 'Post Two', 
        'author' : 'post_author - 2',
        'content' : 'this content is for post two only',
        'date_posted' : '30th Jan 2018',
    }
]


def home(req):
    data = {
        'posts' : posts
    }

    return render(req,'index.html',data)

def profile(req):

    return render(req,'profile.html')
