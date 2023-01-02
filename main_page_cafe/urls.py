from django.urls import path
from .views import view_main_page


urlpatterns = [
    path('', view_main_page, name='main_page'),

]