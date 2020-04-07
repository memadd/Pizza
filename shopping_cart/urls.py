from django.urls import path 
from . import views
app_name = 'cart'
urlpatterns = [
    path('add_to_cart/<str:pk>/', views.add_to_cart, name="add_to_cart"),
]