from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser (AbstractUser):
    sex_choice =((0, "Nữ"),(1,"Nam"),(2,"Không xác định"))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=sex_choice,default=0)
    address = models.CharField(default="",max_length=255)
# Create your models here.

class flowers (models.Model):
    ms = models.CharField(max_length=100)
    name= models.TextField()
    price = models.FloatField()
    image = models.ImageField(null=True)
    description = models.TextField()
    number = models.IntegerField()

class gioHang (models.Model):
    items = models.IntegerField()
    user = models.TextField()
    number = models.IntegerField()
    price = models.FloatField()
    ngay = models.DateField()
    pttt = models.BooleanField(default=False)