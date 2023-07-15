from urllib import request
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .form import newForm

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
def register(register):
    return render(register,'registration/login.html')
# class newStudent(CreateView):
#     model = student
#     template_name ='student_new.html'
#     field ='__all__'
def home_view(request):
    # context ={}
    # context['form']= newForm()
    # return render (request,"pages/student_new.html",context)
    if request.method =="POST":
        form = newForm (request.POST)
        if form.is_valid():
            post = student()
            post.mssv = request.POST['mssv']
            post.name = request.POST['name']
            post.email = request.POST['email']
            post.phone = request.POST['phone']
            post.date = request.POST['date']
            post.save()
            return render (request,"pages/home.html")
    else:
        form = newForm()
        return render (request,"pages/student_new.html",{'form':form})
    

def password(register):
     return render(register,'registration/password_change.html')

def login(register):
     return render(register,'registration/login.html')
