from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
     path('', views.index, name='index'),
     path('abouts', views.about, name='about')
     
]