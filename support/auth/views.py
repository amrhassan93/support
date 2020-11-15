from django.shortcuts import render , redirect
from django.http import HttpResponse
# from auth.models import Book , Auther

# Create your views here.
def view_login(request):
    return render(request ,'login.html')