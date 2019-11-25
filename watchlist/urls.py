from django.urls import path
from . import views

app_name = 'watchlist'

urlpatterns = [
    path('', views.watchlist, name='watchlist'),
    path('book/', views.book, name='book'),
    path('film/', views.film, name='film'),
    path('article/<int:check_id>/', views.check_body, name='check_body'),
]
