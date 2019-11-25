from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),

    path('article/<int:blog_id>/', views.blog_body, name='blog_body'),

    path('programming/', views.programming, name='programming'),
    path('thinking/', views.thinking, name='thinking'),
    path('other/', views.other, name='other'),

    path('search/', views.search, name='search'),

]
