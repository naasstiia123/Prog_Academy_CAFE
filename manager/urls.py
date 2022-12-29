from django.urls import path
from .views import reservations, update, feedback, up_feedback

app_name = 'manager'

urlpatterns = [
    path('reservations', reservations, name='reservations'),
    path('reservations/update/<int:pk>', update, name='update'),
    path('feedback', feedback, name='feedback'),
    path('feedback/update/<int:pk>', up_feedback, name='up_feedback'),
]
