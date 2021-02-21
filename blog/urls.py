from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article, name='article'),
    path('articles/<int:article_id>', views.article_body, name='article_body'),
    path('searchArticles', views.get_search_articles, name='get_search_articles'),
    path('articlesByLabel/<str:label>', views.get_articles_by_label, name='get_articles_by_label'),
    path('articlesByYear/<str:year>', views.get_articles_by_year, name='get_articles_by_year'),
]
