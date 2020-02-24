from django.urls import path

from . import views
app_name = 'users'
urlpatterns = [
    
    path("register/",views.userFormView.as_view(), name='register'),
    path("logout", views.logout_view, name='logout'),
    path("login/", views.login_view, name='login')
    
]