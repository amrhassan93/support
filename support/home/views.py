from django.shortcuts import render , get_object_or_404
from projects.models import Project
# from django.db.models import Q
# Create your views here.

def view_home(request):
    # projects = Project.objects.all()
    highest_five_rated  = Project.objects.all()[:5]

    lastest_five = Project.objects.order_by('start_date')[:5]

    featured_projects = Project.objects.filter(is_featured = True)
    
    context = {
        'highest_five_rated' : highest_five_rated,
        'lastest_five' : lastest_five,
        'featured_projects': featured_projects
        }

    return render(request,'home/home.html',context)


def view_index(request):
    return render(request , 'home/index.html')

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

def search(request):
    keyword = request.GET.get('keyword')
    # search_result =get_object_or_404(Project ,title__contains = keyword)
    search_result = Project.objects.filter(title__contains = keyword)
    return render(request , 'home/search.html' ,{"search_result" : search_result})