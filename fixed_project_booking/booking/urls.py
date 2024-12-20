from django.urls import path
from . import views

urlpatterns = [
    path(
        'fields/availability/', 
        views.get_field_availability, 
        name='field_availability'
    ),
    path('', views.home, name='home'),
]
