from django.db import models
from django.utils import timezone

# Create your models here.


class Users(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    passowrd= models.CharField(max_length=100)
    mobile_number= models.IntegerField()
    avatar= models.ImageField()
    email= models.EmailField(max_length=100)
    Provider = models.CharField(
        max_length=50 ,
        choices=[
            ('mail' , 'email'),
            ('facebook' , 'facebook')
        ])
    country= models.CharField(max_length=50 , null=True)
    birth_date= models.DateField(null=True)
    facebook_profile = models.CharField(max_length=100 , null=True)
    is_admin = models.BooleanField(default=False)
    is_acive = models.BooleanField(default=False)

    def _str_(self):
        return self.first_name