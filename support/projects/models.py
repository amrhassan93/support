import datetime
from django.db import models
from django.utils import timezone
from reglogin.models import Users

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField(max_length=50)

    def _str_(self):
        return self.cat_name

class Tags(models.Model):
    tag_name = models.CharField(max_length=50)

    def _str_(self):
        return self.tag_name


class Project(models.Model):
    title= models.CharField(max_length=100)
    details= models.CharField(max_length=1000)
    target= models.FloatField()
    created_at= models.DateField(timezone.now())
    start_date= models.DateField()
    end_date= models.DateField()
    images = models.ImageField()
    total_rate = models.FloatField()
    is_featured = models.BooleanField(default=False)
    user_id = models.ForeignKey(Users , on_delete = models.CASCADE)
    category_id = models.ForeignKey(Category , on_delete = models.CASCADE)

    def _str_(self):
        return self.title

class Rating(models.Model):
    rate = models.FloatField()
    project_id = models.ForeignKey(Project , on_delete = models.CASCADE)
    user_id = models.ForeignKey(Users , on_delete = models.CASCADE)
    


class Donation(models.Model):
    donation_amount = models.FloatField()
    project_id = models.ForeignKey(Project , on_delete = models.CASCADE)
    user_id = models.ForeignKey(Users , on_delete = models.CASCADE)

class ProjectTag(models.Model):
    project_id = models.ForeignKey(Project , on_delete = models.CASCADE)
    tag_id = models.ForeignKey(Tags , on_delete = models.CASCADE)

class Comments(models.Model):
    comment_body = models.CharField(max_length=500)
    project_id = models.ForeignKey(Project , on_delete = models.CASCADE)
    user_id = models.ForeignKey(Users , on_delete = models.CASCADE)


class CommentReply(models.Model):
    reply_body = models.CharField(max_length=500)
    comment_id = models.ForeignKey(Comments , on_delete = models.CASCADE)
    user_id = models.ForeignKey(Users , on_delete = models.CASCADE)



# 1- create db lacaly  => create database support_app
# 2- python manage.py makemigrations 
# 3- python3 manage.py migrate
