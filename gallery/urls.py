from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('remove/', views.remove, name='remove'),
     path('remove/<int:pro_idea>', views.remove, name='remove'),
    path('filters/', views.filters, name='filters'),
    path('view/', views.view, name='view'),
]
