from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('change_pwd/', views.change_pwd, name='change_pwd'),
    path('reset_pwd/', views.reset_pwd, name='reset_pwd'),
]
