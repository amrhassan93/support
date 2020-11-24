from django.contrib import admin
from django.urls import path
from home.views import view_index, view_home
 

urlpatterns = [
    path('' , view_index),
    path('home' , view_home),
    # path('createhome',create_home)
]