from django.shortcuts import render
from .models import Category,Project,Rating,Donation,ProjectPicture,Comments,CommentReply,ProjectReport,CommentReport
from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectsForm, ImageForm
from django.http.response import HttpResponse,JsonResponse,HttpResponseForbidden
from django.forms import modelformset_factory
from django.contrib import messages
from django.db.models import Q, Avg, Sum
from taggit.models import Tag
from decimal import Decimal, ROUND_HALF_UP
from django.template.loader import render_to_string
from datetime import datetime
from reglogin.models import Users
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.

def all_project(request):
    projects = Project.objects.all()
    context = {
        'projects' : projects
    }
    return render(request , 'projects/all_projects.html' , context)

def showProject(request, id):
    item = Project.objects.get(id=id)
    pPics = ProjectPicture.objects.filter(project_id=id)
    relatedProjects = Project.objects.all().filter(category_id=item.category_id)
    today = datetime.now()
    start_date = item.start_date
    end_date = item.end_date
    myFormat = "%Y-%m-%d %H:%M:%S"
    today = today.strftime(myFormat)
    today = datetime.strptime(today, "%Y-%m-%d %H:%M:%S")
    start_date = start_date.strftime(myFormat)
    start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_date = end_date.strftime(myFormat)
    end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    donate = item.donation_set.all().aggregate(Sum("donation_amount"))
    context = {'pData': item,
               'pPics': pPics,
               'today': today,
               'start_date': start_date,
               'end_date': end_date,
               'relatedProjs': relatedProjects,
               'donations_amount': donate["donation_amount__sum"] if donate["donation_amount__sum"] else 0}
   
    return render(request, "projects/view_project.html", context)

@login_required()
def create(request):

    ImageFormSet = modelformset_factory(
        ProjectPicture, form=ImageForm, min_num=1, extra=3)

    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=ProjectPicture.objects.none())

        if form.is_valid() and formset.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
            form.save_m2m()
            for form in formset.cleaned_data:
                if form:
                    image = form['img_url']
                    photo = ProjectPicture(project_id=new_form, img_url=image)
                    photo.save()
            return redirect(f'/projects/projectDetails/{new_form.id}')
        context = {
            'form': form,
            'formset': formset,
        }
        return render(request, 'projects/create.html', context)
    else:

        form = ProjectsForm()
        formset = ImageFormSet(queryset=ProjectPicture.objects.none())
        context = {
            'form': form,
            'formset': formset,
        }
    return render(request, 'projects/create.html', context)



@login_required()
def delete_project(request, pk):

    project = Project.objects.get(id=pk)
    project.delete()
    return render(request,'projects/all_projects.html' )

@login_required()
def delete_comment(request,comment_id,project_id):
    Comments.objects.get(id=comment_id).delete()
    return redirect(f'/projects/projectDetails/{project_id}')


@login_required()
def edit_comment(request, comment_id, project_id):
    project = Project.objects.filter(pk=project_id)[0]
    comment = Comments.objects.filter(id=comment_id)[0]
    context= { 'comment': comment,
    'project': project}
    return render(request, 'editcomment.html',context)

@login_required()
def update_comment(request, comment_id, project_id):
    content = request.POST['content']
    Comments.objects.filter(pk=comment_id).update(content=content)
    return redirect(f'/projects/projectDetails/{project_id}')
@login_required()
def report_comment(request, comment_id, project_id):
    user_id = request.user
    user_test = Users.objects.get(user_id = user_id)
    user1 = Users.objects.filter(id=user_test.id)[0]
    comment1=Comments.objects.filter(pk=comment_id)[0]

    report_comment =CommentReport (
        user_id=user1,
        comment_id=comment1)
    report_comment.save()
    return redirect(f'/projects/projectDetails/{project_id}')



@login_required()
def report_project(request, project_id):
    user_id = request.user
    user_test = Users.objects.get(user_id = user_id)
    user1 = Users.objects.filter(id=user_test.id)[0]
    Project1=Project.objects.filter(pk=project_id)[0]
    report_project = ProjectReport(
        user_id=user1,
        project_id=Project1)
    report_project.save()
    return redirect(f'/projects/projectDetails/{project_id}')
@login_required()
def donate(request,id):
    if request.user.is_authenticated: 
        user_id = request.user
        user_test = Users.objects.get(user_id = user_id) 
        user1 = Users.objects.filter(id=user_test.id)[0]
        p1=Project.objects.filter(id=id)[0]
        if request.method == 'POST':
            donate = Donation.objects.create(
                donation_amount=request.POST['donate'],
                project_id=p1,
                user_id=user1
            )
            return redirect(f'/projects/projectDetails/{id}')
    else:
        return redirect(f'/projects/projectDetails/4')


def show_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)

    projects = Project.objects.filter(tags=tag)
    context = {
        'tag': tag,
        'projects': projects,
    }
    return render(request, 'projects/tag.html', context)



def showCategoryProjects(request, id):
    cate = Category.objects.get(id=id)
    context = {'catname': cate}
    return render(request, "projects/viewCategory.html", context)


def list_categories(request):

     cates = Category.objects.all()
     return {
        'categs': cates
      }




@login_required()
def create_comment(request,id):
    user_id = request.user
    user_test = Users.objects.get(user_id = user_id)
    user1 = Users.objects.filter(id=user_test.id)[0]
    p1=Project.objects.filter(id=id)[0]
    comment = Comments()
    comment.content = request.POST['content']
    comment.project_id = p1
    comment.user_id = user1
    comment.save()
    return redirect(f'/projects/projectDetails/{id}')






