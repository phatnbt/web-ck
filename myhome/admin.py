from django.contrib import admin
from .models import student
from .models import teachers,CustomUser
from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
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

class CustomUserAdmin (UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
admin.site.register(CustomUser,CustomUserAdmin)