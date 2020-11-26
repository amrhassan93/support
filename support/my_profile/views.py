from django.shortcuts import render, redirect
from django.http import HttpResponse
from projects.models import Donation, Project
from reglogin.models import Users
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

def all_project(request):
    user = User.objects.get(id=request.session['id'])
    all_project = Project.objects.all().filter(user_id = user)
    
    context = {
      'all_project' : all_project,
    }
    # return HttpResponse(all_project.project_title)
    if 'id' in request.session:
        return render(request,'all_project.html',context)
    else:
        return  redirect('/login')

class ProjectListView(ListView):
  model = Project
  template_name = "my_profile/all_project.html"
  context_object_name = 'all_project'
  ordering = ['-date-posted']




def detail_view(request, id):
  details = Project.objects.get(id = id)
  context ={
    "details":details
  } 
  return render(request, "home/post_detail.html",context)


class ProjectDetaiView(DetailView):
  model = Project


# def all_donation(request):
#     user = User.objects.get(id=request.session['id'])
#     all_donation = Donation.objects.all().filter(user_id = user)
    
#     context = {
#       'all_donation' : all_donation,
#     }
#     if 'id' in request.session:
#         return render(request, 'all_donation.html', context)
#     else:
#         return redirect('/login')
