from django.urls import path
from .views import PostListView, PostCreateView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('home/', PostListView.as_view(), name='home'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),

]
