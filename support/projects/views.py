from django.shortcuts import render
from .models import *
from django.forms import modelformset_factory
import json
import re
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProjectsForm, ImageForm
from django.http.response import HttpResponse, JsonResponse,HttpResponseForbidden
from django.forms import modelformset_factory
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.db.models import Q, Avg, Sum
# Create your views here.
from taggit.models import Tag
from decimal import Decimal, ROUND_HALF_UP
from django.template.loader import render_to_string
from datetime import datetime


# Create your views here.

def all_project(request):
    return render(request , 'projects/all_projects.html')

def showProject(request, id):
    # item = Project.objects.get(id=id)
    # pPics = ProjectPicture.objects.all().filter(project_id=id)
    # relatedProjects = Project.objects.all().filter(category_id=item.category)
    # rate = item.rate_set.all().aggregate(Avg("value"))["value__avg"]
    # rate = rate if rate else 0
    # rate = Decimal(rate).quantize(0, ROUND_HALF_UP)
    # today = datetime.now()
    # start_date = item.start_date
    # end_date = item.end_date
    # myFormat = "%Y-%m-%d %H:%M:%S"
    # today = today.strftime(myFormat)
    # today = datetime.strptime(today, "%Y-%m-%d %H:%M:%S")
    # start_date = start_date.strftime(myFormat)
    # start_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    # end_date = end_date.strftime(myFormat)
    # end_date = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")
    # donate = item.donation_set.all().aggregate(Sum("amount"))
    # context = {'pData': item,
    #            'pPics': pPics,
    #            'rate': rate,
    #            'today': today,
    #            'start_date': start_date,
    #            'end_date': end_date,
    #            'relatedProjs': relatedProjects,
    #            'donations_amount': donate["amount__sum"] if donate["amount__sum"] else 0}

    # if request.user:
    #     user_rate = item.rate_set.filter(
    #         user_id=request.user.profile.id).first()
    #     if user_rate:
    #         context["user_rate"] = user_rate.value
    return render(request, "projects/view_Project.html", context)

def create(request):

    ImageFormSet = modelformset_factory(
        ProjectPicture, form=ImageForm, min_num=1, extra=3)

    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=ProjectPicture.objects.none())

        if form.is_valid() and formset.is_valid():
            new_form = form.save(commit=False)
            # new_form.user = Profile.objects.get(user=request.user)
            new_form.save()
            form.save_m2m()
            for form in formset.cleaned_data:
                if form:
                    image = form['img_url']
                    photo = ProjectPicture(Project=new_form, img_url=image)
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



