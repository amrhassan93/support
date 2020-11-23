from django.contrib import admin
from django.urls import path
from . import views
 

urlpatterns = [
    path('' , views.all_project),
    path('create/', views.create),
    path('projectDetails/<int:id>',views.showProject,name="show_proj"),
 
]