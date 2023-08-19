from urllib import request
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .form import newForm
from .models import flowers

# Create your views here.
from django.http import HttpResponse
def list_flowers (request):
    Data1 ={'flowers':flowers.objects.all()}
    return render (request,'pages/flowers.html',Data1)
def home_page (request):
    Data1 ={'flowers':flowers.objects.all()}
    return render (request,'nguoidung/home.html',Data1)

def pan(contact):
    return render(contact,'pages/contact.html')
def list_id(request,id):
    flower= flowers.objects.get(id=id)
    return render (request,'pages/detail.html',{"flowers":flower})

def error(error):
    return render(error,'pages/error.html')
def register(register):
    return render(register,'registration/login.html')

def home_view(request):
    if request.method =="POST":
        form = newForm(request.POST, request.FILES)
        if not form.is_valid():
            post = flowers()
            post.ms = request.POST['ms']
            post.name = request.POST['name']
            post.price = request.POST['price']
            post.image = request.POST['image']
            post.description = request.POST['description']
            post.number = request.POST['number']
            post.save()
            return render (request,"pages/success.html")
    else:
        form = newForm()
        return render (request,"pages/flowers_new.html", {'form':form})


def flowers_id(request, id):
    Flowers = flowers.objects.get(id=id)
    return render(request, 'pages/detail.html', {'flowers':Flowers})


def flower_detail(request, id):
    Flower = flowers.objects.get(id=id)
    return render(request, 'nguoidung/detail_flower.html', {'flower':Flower})

def login(register):
     return render(register,'registration/login.html')

def delete_item(request, id):
    item = flowers.objects.get(id=id)
    item.delete()
    return render(request, 'pages/delete.html')
