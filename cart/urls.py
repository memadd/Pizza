from django.urls import path

from .views import *

app_name = 'cart'

urloatterns = [
    path('add_to_cart/<str:pk>/', add_to_cart, name='add_to_cart'),
]