from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.
def view_profile(request):
    return render(request ,'profile.html')


def edit_profile(request):
    return render(request,'edit.html')