from django.contrib import admin
from .models import student
from .models import teachers

class StudentAdmin (admin.ModelAdmin):
    list_display =['id','mssv','date','name']
    list_filter= ['name']
    search_fields =['name','majors']
admin.site.register(student, StudentAdmin)

# Register your models here.

class TeacherAdmin (admin.ModelAdmin):
    list_display =['date','name','id']
    # list_filter= ['name']
    # search_fields =['name']
admin.site.register(teachers, TeacherAdmin)