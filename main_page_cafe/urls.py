from django.contrib import admin
from django.urls import path
import views

urlpatterns = [
    path('', views.view_main_page),
]