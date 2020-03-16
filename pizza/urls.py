
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include('orders.urls')),
    path("", include('users.urls')),
    path("", include('cart.urls')),
    path("admin/", admin.site.urls),
]
