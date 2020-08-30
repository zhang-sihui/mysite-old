from django.urls import path, re_path
from . import views

app_name = 'polls'

urlpatterns = [
    path('voteList', views.IndexView.as_view(), name='vote'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/result', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),

    path('upload', views.upload_file, name='upload_file'),
    path('uploaded', views.uploaded_files, name='uploaded_files'),
    path('show', views.show_files, name='show_files'),
    re_path('download/(?P<file_id>\\d+)/', views.download_file, name='download_file'),

    path('musicIndex', views.play_music, name='play_music'),
    path('musicLyric/<str:filename>', views.get_music_lyric, name='get_music_lyric'),
]
