from django.urls import path

from . import views
app_name = 'orders'
urlpatterns = [
    path("", views.index, name="index"),
    path("register/",views.userFormView.as_view(), name='register')
]
