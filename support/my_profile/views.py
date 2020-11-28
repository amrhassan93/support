from django.shortcuts import render , redirect
from django.http import HttpResponse
from projects.models import Project
from reglogin.models import Users


# Create your views here.
def view_profile(request ,id):
    user_profile = Users.objects.get(id = id)
    user_projects = Project.objects.filter(user_id = id)
    context = {
        'user' : user_profile,
        'user_projects':user_projects
    }
    return render(request ,'profile.html' , context)


def edit_profile(request , id):
    if request.method == 'POST':
        user_profile = Users.objects.get(id = id)
        user_profile.first_name = request.POST['first_name']
        user_profile.last_name = request.POST['last_name']
        user_profile.mobile_number = request.POST['mobile_number']
        user_profile.birth_date = request.POST['birth_date']
        user_profile.country = request.POST['country']
        user_profile.facebook_profile = request.POST['facebook_profile']
        user_profile.save()
        

        user_profile = Users.objects.get(id = id)
        context = {
            'user' : user_profile
        }

        return render(request,'profile.html' , context) 

    else:
        user_profile = Users.objects.get(id = id)
        context = {
            'user' : user_profile
        }
        return render(request,'edit.html' , context)


def delete_profile(request , id):
    del_user = Users.objects.get(id = id)
    del_user.delete()
    return redirect('/home/')