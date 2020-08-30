from django.urls import path
from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.watchlist, name='watchlist'),
    path('books', views.get_books, name='get_books'),
    path('films', views.get_films, name='get_films'),
    path('checklists/<int:check_id>', views.check_body, name='check_body'),
]
