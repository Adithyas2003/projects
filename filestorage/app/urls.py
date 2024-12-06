from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('login',views.e_login),
    path('register',views.register),
    path('logout',views.e_logout),
    path('file_view/', views.file_list, name='file_view'),
    path('file_add/', views.file_upload, name='file_add'),
   
   


   
]