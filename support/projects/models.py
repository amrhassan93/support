from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager
from django.core.validators import MaxValueValidator, MinValueValidator
from reglogin.models import Users


# from Users.models import Profile




class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    cat_icon = models.ImageField(upload_to='static/projects/images/', default=True)


    def _str_(self):
        return self.cat_name


class Project(models.Model):
    
    title = models.CharField(max_length=45)
    details = models.TextField(max_length=3000)
    target = models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    is_featured = models.BooleanField(default=False)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('title',)


class Rating(models.Model):
    value = models.IntegerField(default=1,validators=[MaxValueValidator(100), MinValueValidator(1)])
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    


class Donation(models.Model):
    donation_amount = models.IntegerField()
    project_id = models.ForeignKey(Project , on_delete = models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

class ProjectPicture(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, default=None, related_name='imgs')   
    img_url = models.ImageField(upload_to='static/projects/images/', verbose_name='Image')

   
    


class Comments(models.Model):
    
    content = models.TextField(max_length=3000, blank=False,default="some string")
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    

class CommentReply(models.Model):
    reply_body = models.CharField(max_length=500)
    comment_id = models.ForeignKey(Comments , on_delete = models.CASCADE)
    user_id = models.ForeignKey(Users , on_delete = models.CASCADE)


class ProjectReport(models.Model):
    content = models.TextField(max_length=3000)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


class CommentReport(models.Model):
    comment_id = models.ForeignKey(Comments, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)


# 1- create db lacaly  => create database support_app
# 2- python manage.py makemigrations 
# 3- python3 manage.py migrate