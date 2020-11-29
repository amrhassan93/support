from django.contrib import admin
from django.urls import path
from reglogin.views import register,loginform,activate_account
from django.conf.urls import url

 
urlpatterns = [
    path('login' ,loginform, name='login'),
    path('signup' ,register, name='signup'),
    path('activate/<uidb64>/<token>',activate_account, name='activate')
]
  