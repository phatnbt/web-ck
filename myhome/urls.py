from django.urls import path
from .import views


urlpatterns =[
    path('/home',views.list),
    path('/contact',views.pan),
    path('/error',views.error),
    path('/teachers',views.list_teachers),
    path('/home/<int:id>',views.list_id),
    path('/teachers/<int:id>',views.list_id1),
]