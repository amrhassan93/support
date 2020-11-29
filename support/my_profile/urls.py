from django.contrib import admin
from django.urls import path
from my_profile.views import view_profile , edit_profile , delete_profile

urlpatterns = [
    path('<id>' ,view_profile , name='profile'),
    path('edit/<id>' ,edit_profile , name='edit'),
    path('delete/<id>' ,delete_profile , name='delete'),

]