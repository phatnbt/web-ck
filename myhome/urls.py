from django.urls import path,include
from .import views
from django.views.generic.base import TemplateView


urlpatterns =[
    path('/accounts/',include('django.contrib.auth.urls')),
    path('/student/new/', views.home_view ,name='student_new'),
    path('/home',views.list),
    path('/contact',views.pan),
    path('/error',views.error),
    path('/teachers',views.list_teachers),
    path('/home/<int:id>',views.list_id),
    path('/teachers/<int:id>',views.list_id1),
    path ('/pass/',views.password),
    # path('/logout/',views.login, name='logout'),
    # path('/login/',views.list_teachers,name='login'),
]