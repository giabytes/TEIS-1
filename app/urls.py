from django.urls import path
from . import views

urlpatterns = [
    path('', views.flights_list, name='flights_list'),
    path('flights_list/', views.flights_list, name='flights_list'),
    path('flights_register/', views.flights_register, name='flights_register'),
    path('flights_statistics/', views.flights_statistics, name='flights_statistics'),
]