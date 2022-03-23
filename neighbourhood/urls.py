from django.urls import path  
from django.contrib import admin  
from . import views  
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static

urlpatterns=[
     path('',views.index, name='index'),
     path('logout/',views.logout_request,name='logout'),
     path('new/business',views.new_business,name='new-business'),
     path('profile/',views.profile,name='profile'),
     path('new_profile',views.new_profile,name = 'new_profile'),
     path('edit/profile/',views.profile_edit,name = 'edit_profile'),
     path('business_list/',views.business,name='business'),
     path('search/',views.search_post, name='search_results'),
     path('contact-us/',views.contact, name='contact-us'),
     path('new_post/',views.new_post,name='create-post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
