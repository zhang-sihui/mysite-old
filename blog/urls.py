from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('articles/<int:blog_id>', views.blog_body, name='blog_body'),
    path('search', views.search, name='search'),
    path('displayLabels', views.display_label, name='display_label'),
    path('blogsByLabel/<str:label>', views.get_blog_by_label, name='get_blog_by_label'),
]
