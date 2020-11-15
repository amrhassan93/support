from django.contrib import admin
from django.urls import path
from home.views import view_index 

 

urlpatterns = [
    path('index' , view_index),
]