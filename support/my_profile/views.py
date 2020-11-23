from django.shortcuts import render , redirect
from django.http import HttpResponse
from project.models import *
from reglogin.models import Users

# Create your views here.
def view_profile(request):
    return render(request ,'profile.html')


def edit_profile(request):
    return render(request,'edit.html')



def all_project(request):
    user = Users.objects.get(id=request.session['id'])
    all_project = Project.objects.all().filter(user_id = user)
    
    context = {
      'all_project' : all_project,
    }
    # return HttpResponse(all_project.project_title)
    if 'id' in request.session:
        return render(request,'all_project.html',context)
    else:
        return  redirect('/login')



def all_donation(request):
    user =User.objects.get(id=request.session['id'])
    all_donation =Donation.objects.all().filter(user_id = user)
    
    context = {
      'all_donation' : all_donation,
    }
    if 'id' in request.session:
        return render(request, 'all_donation.html', context)
    else:
        return redirect('/login')
