from django.urls import path
import main_page_cafe.views

urlpatterns = [
    path('', main_page_cafe.views.view_main_page),
]