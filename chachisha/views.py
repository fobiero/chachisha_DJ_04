from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView


def index(req) :
    return render (req, 'index.html')

# @TODO:get all posts 
@login_required
def home(req):
    context = {
        'posts' : Post.objects.all()
    }

    return render(req,'home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['date_posted']

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content','image']

