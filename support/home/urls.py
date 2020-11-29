from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from home.views import view_index , view_home , search
 

urlpatterns = [
    path('' , view_home),
    path('home' , view_index),
    path('search/<keyword>', search)

=======
from home.views import  view_index, view_home , search

urlpatterns = [
    path('' , view_home, name='home'),
    path('home' , view_index ),
    path('search/', search , name ='search')
    # path('createhome',create_home)
>>>>>>> 16794e705e0f12119669828544ad2794632db66e
]