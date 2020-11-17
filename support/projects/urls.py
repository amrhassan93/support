from django.contrib import admin
from django.urls import path
from projects.views import all_project,view_project
 

urlpatterns = [
    path('' , all_project),
    path('project/',view_project),
]