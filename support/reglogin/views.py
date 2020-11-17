from django.shortcuts import render , redirect
from django.http import HttpResponse
# from {}.models import 

# Create your views here.
def view_login(request):
    return render(request ,'login.html')

def view_signup(request):
    return render(request ,'signup.html')

def upload(request):
    return render(request ,'')