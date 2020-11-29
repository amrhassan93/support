from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import Users
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name= models.CharField(max_length=100)
    # last_name= models.CharField(max_length=100)
    # passowrd= models.CharField(max_length=100)
    mobile_number= models.IntegerField(null=True)
    avatar= models.ImageField(null=True)
    # email= models.EmailField(max_length=100)
    Provider = models.CharField(
        null=True,
        max_length=50 ,
        choices=[
            ('mail' , 'email'),
            ('facebook' , 'facebook')
        ])
    country= models.CharField(max_length=50 , null=True)
    birth_date= models.DateField(null=True)
    facebook_profile = models.CharField(max_length=100 , null=True)
    # is_admin = models.BooleanField(default=False)
    # is_acive = models.BooleanField(default=False)

    # def _str_(self):
    #     return self.first_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.users.save()


    
# class Users(models.Model):
#     first_name= models.CharField(max_length=100)
#     last_name= models.CharField(max_length=100)
#     passowrd= models.CharField(max_length=100)
#     # phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$',
#     #                              message="Phone number must match egyptian format")
#     mobile_number= models.IntegerField(blank=True)
#     image = models.ImageField(blank=True, null=True)
#     email= models.EmailField(max_length=100)
#     Provider = models.CharField(
#         max_length=50 ,
#         choices=[
#             ('mail' , 'email'),
#             ('facebook' , 'facebook')
#         ])
#     country= models.CharField(max_length=50 , null=True)
#     birth_date= models.DateField(null=True)
#     facebook_profile = models.URLField(blank=True,null=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     def _str_(self):
#         return self.first_name
