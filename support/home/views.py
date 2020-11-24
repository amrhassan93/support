from django.shortcuts import render
from projects.models import Project
# from django.db.models import Q
# Create your views here.

def view_index(request):
    projects = Project.objects.all()
    highest_five_rated  = Project.objects.all()[:5]

    lastest_five = Project.objects.order_by('-start_time')[:5]

    featured_projects = Project.objects.filter(Featured = True)
    
    context = {
        'highest_five_rated' : highest_five_rated,
        'lastest_five' : lastest_five,
        'featured_projects': featured_projects
        }

    return render(request,'home/index.html',context)


def view_home(request):
    return render(request , 'home/home.html')

# def create_home(request):
#     return render(request, 'home/create_home.html')    


 # # 'title' : title,
        # # 'details': details,
        # # 'target': target,
        # # 'created_at': created_at,
        # # 'start_date': start_date,
        # # 'end_date': end_date,
        # # 'images': images,
        # # 'total_rate': total_rate,
        # # 'is_featured': is_featured,
        # # 'user_id': user_id
        # 'projects':projects