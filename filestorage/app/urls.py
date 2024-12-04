from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('login',views.e_login),
    path('register',views.register),
    path('logout',views.e_logout),


   
]