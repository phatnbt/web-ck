from django.contrib import admin
from .models import CustomUser
from .form import CustomUserCreationForm, CustomUserChangeForm
# from .models import CustomUser
from .models import flowers
from django.contrib.auth.admin import UserAdmin
# class StudentAdmin (admin.ModelAdmin):
#     list_display =['id','mssv','date','name']
#     list_filter= ['name']
#     search_fields =['name','majors']
# admin.site.register(student, StudentAdmin)

# # Register your models here.

class FlowerAdmin (admin.ModelAdmin):
    list_display =['id','ms','name','price']
    list_filter= ['name']
    search_fields =['name']
admin.site.register(flowers, FlowerAdmin)

class CustomUserAdmin (UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
admin.site.register(CustomUser,CustomUserAdmin)