from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('menu/', views.menu),
    path('services/', views.services),
    path('about/', views.about),
    path('contact/', views.contact),
]
