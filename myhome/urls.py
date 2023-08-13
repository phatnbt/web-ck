from django.urls import path,include
from .import views
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('/accounts/',include('django.contrib.auth.urls')),
    path('/flowers/create', views.home_view ,name='flowers_new'),
    path('/home',views.list_flowers),
    path('/home_page',views.home_page),
    # path('/contact',views.pan),
    # path('/error',views.error),
    # path('/teachers',views.list_teachers),
    path('/home/<int:id>',views.list_id),
    path('/flowers/<int:id>',views.flowers_id),
    path('/flower_detail/<int:id>',views.flower_detail),
    path('/flowers/delete/<int:id>/', views.delete_item, name='delete_item'),
    # path ('/pass/',views.password),
    # path('/logout/',views.login, name='logout'),
    # path('/login/',views.list_flowers,name='login'),
     path('/reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('/reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]