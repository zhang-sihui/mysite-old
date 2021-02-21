from django.urls import path, re_path
from . import views

app_name = 'files'

urlpatterns = [
    path('', views.files, name='files'),
    path('upload', views.upload_file, name='upload_file'),
    path('uploaded', views.uploaded_files, name='uploaded_files'),
    re_path('download/(?P<file_id>\\d+)/', views.download_file, name='download_file'),
]
