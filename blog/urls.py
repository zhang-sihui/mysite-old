from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('articles/<int:blog_id>', views.blog_body, name='blog_body'),
    path('searchBlogs', views.search_blogs, name='search_blogs'),
    path('blogsByLabel/<str:label>', views.get_blogs_by_label, name='get_blogs_by_label'),
    path('blogsByYear/<str:year>', views.get_blogs_by_year, name='get_blogs_by_year'),
]
