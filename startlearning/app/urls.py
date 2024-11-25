from django.urls import path
from . import views


urlpatterns = [
    path('', views.e_shop_login),
    path('contact/', views.contact),
    path('about/',views.about),
    path('courses/',views.courses)
]
