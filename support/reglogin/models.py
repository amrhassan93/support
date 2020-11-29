from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number= models.IntegerField(null=True)
    avatar= models.ImageField(null=True)
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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Users.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.users.save()
