from django.contrib import admin
from django.urls import path
from reglogin.views import view_login
 
urlpatterns = [
    path('login' ,view_login),
]
  