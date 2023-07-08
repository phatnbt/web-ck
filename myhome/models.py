from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser (AbstractUser):
    sex_choice =((0, "Nữ"),(1,"Nam"),(2,"Không xác định"))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=sex_choice,default=0)
    address = models.CharField(default="",max_length=255)
# Create your models here.
class student (models.Model):
    mssv =models.CharField(max_length=100)
    name= models.TextField()
    email = models.TextField()
    phone = models.CharField(max_length=10)
    date = models.CharField(max_length=100)
    gender = models.TextField()
    address = models.TextField()
    ethnic = models.TextField()
    department =models.TextField()
    majors = models.TextField()
    classroom = models.CharField(max_length=1000)

class teachers (models.Model):
    msgv =models.CharField(max_length=100)
    name= models.TextField()
    email = models.TextField()
    phone = models.CharField(max_length=100)
    date = models.CharField(max_length=100)