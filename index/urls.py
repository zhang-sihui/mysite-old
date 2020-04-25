from django.urls import path
from . import views


app_name = 'index'

urlpatterns = [
    # main
    path('', views.index, name='index'),
    path('about_me', views.about_me, name='about_me'),
]
