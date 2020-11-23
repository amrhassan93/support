from django.contrib import admin
from django.urls import path
from my_profile.views import view_profile,edit_profile
 
urlpatterns = [
    path('' ,view_profile),
    path('edit.html',edit_profile),
    
]