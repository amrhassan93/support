from django.contrib import admin
from django.urls import path
from auth.views import view_login
 
urlpatterns = [
    path('login' ,view_login),
]
  