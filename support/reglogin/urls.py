from django.contrib import admin
from django.urls import path
from reglogin.views import view_login,view_signup,upload
 
urlpatterns = [
    path('login' ,view_login),
    path('signup' ,view_signup)
]
  