from django.db import models

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