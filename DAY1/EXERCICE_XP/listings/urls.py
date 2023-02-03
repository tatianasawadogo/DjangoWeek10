from django.urls import path,include
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>/listing', views.listing, name='listing'),
    path('search', views.search, name='search'),

   
]