from django.urls import path
from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.get_watchlists, name='get_watchlists'),
    path('books', views.get_books, name='get_books'),
    path('films', views.get_films, name='get_films'),
    path('reviews/<int:review_id>', views.get_reviews, name='get_reviews'),
]
