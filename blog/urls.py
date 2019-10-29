from django.urls import path, re_path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('programming/', views.programming, name='programming'),
    path('thinking/', views.thinking, name='thinking'),
    path('other/', views.other, name='other'),

]