from django.urls import path 
from . import views
app_name = 'cart'
urlpatterns = [
    path('add_to_cart/<str:pk>/', views.add_to_cart, name="add_to_cart"),
    path('order_summary/', views.order_details, name="order_summary"),
    path('delete_item/<str:pk>/', views.delete_from_cart, name="delete_item"),
]