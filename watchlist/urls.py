from django.urls import path
from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.watchlist, name='watchlist'),
    path('books', views.book, name='book'),
    path('films', views.film, name='film'),
    path('articles/<int:check_id>', views.check_body, name='check_body'),
]
