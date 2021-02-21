from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.play_music, name='play_music'),
    path('musicLyric/<str:filename>', views.get_music_lyric, name='get_music_lyric'),
]
