from django.shortcuts import render

# Create your views here.

def view_index(request):
    return render(request , 'home/index.html')

def view_home(request):
    return render(request , 'home/home.html')