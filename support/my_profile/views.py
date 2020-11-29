from django.shortcuts import render , redirect
from django.http import HttpResponse
from projects.models import Project
from reglogin.models import Users
from django.contrib.auth.models import User



# Create your views here.
def view_profile(request ,id):
    user_profile = Users.objects.all().get(id = id)
    auth_user = User.objects.get(id = user_profile.user_id)
    user_projects = Project.objects.filter(user_id = id)
    context = {
        'user' : user_profile,
        'auth_user':auth_user,
        'user_projects':user_projects
    }
    return render(request ,'profile.html' , context)


def edit_profile(request , id):
    if request.method == 'POST':
        user_profile = Users.objects.get(id = id)
        auth_user = User.objects.get(id = user_profile.user_id)
        user_profile.mobile_number = request.POST['mobile_number']
        user_profile.birth_date = request.POST['birth_date']
        user_profile.country = request.POST['country']
        user_profile.facebook_profile = request.POST['facebook_profile']
        user_profile.save()

        auth_user.first_name = request.POST['first_name']
        auth_user.last_name = request.POST['last_name']
        auth_user.save()
        

       

        return redirect(f'/profile/{id}') 

    else:
        user_profile = Users.objects.get(id = id)
        auth_user = User.objects.get(id = user_profile.user_id)

        context = {
            'user' : user_profile,
            'auth_user':auth_user,
        }
        return render(request,'edit.html' , context)


def delete_profile(request , id):
    del_user = Users.objects.get(id = id)
    del_user.delete()
    return redirect('/home/')