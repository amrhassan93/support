from django.contrib import admin
from django.urls import path
from projects.views import all_project
 

urlpatterns = [
    path('' , all_project),
]