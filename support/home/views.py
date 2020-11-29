from django.shortcuts import render , get_object_or_404
from projects.models import Project
# Create your views here.



def view_home(request):
     highest_five_rated = Project.objects.all()[:5]
     lastest_five = Project.objects.order_by('-created_at')[:5]
     featured_projects = Project.objects.filter(is_featured = True)
     context = {
          'highest_five_rated': highest_five_rated,
          'lastest_five': lastest_five,
          'featured_projects': featured_projects
      }
     return render(request,'home/home.html',context)


def view_index(request):
    return render(request , 'home/index.html')


 

def search(request):
    keyword = request.GET.get('keyword')
    search_result = Project.objects.filter(title__contains = keyword)
    return render(request , 'home/search.html' ,{"search_result" : search_result})
