from django.contrib import admin
from django.urls import path
from home.views import  view_index, view_home , search

urlpatterns = [
    path('' , view_home, name='home'),
    path('home' , view_index ),
    path('search/', search , name ='search')
    
]