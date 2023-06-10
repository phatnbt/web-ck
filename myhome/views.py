from urllib import request
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import student
from .models import teachers
def list (request):
    Data ={'students':student.objects.all().order_by('-date')}
    return render (request,'pages/home.html',Data)
def list_teachers (request):
    Data1 ={'teachers':teachers.objects.all()}
    return render (request,'pages/teachers.html',Data1)


def index(request):
    return render(request, 'pages/home.html')
def pan(contact):
    return render(contact,'pages/contact.html')
def list_id(request,id):
    Student= student.objects.get(id=id)
    return render (request,'pages/detail.html',{"Student":Student})
def list_id1(request,id):
    Teacher= teachers.objects.get(id=id)
    return render (request,'pages/detail2.html',{"Teacher":Teacher})
def error(error):
    return render(error,'pages/error.html')
