from django.urls import path,include
from .import views
from django.views.generic.base import TemplateView


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
    path('/register', views.register, name='register'),
    path('/cart',views.cart, name='cart'),
]