from django.urls import path, re_path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.display_photo, name='display'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    re_path('download/(?P<photo_id>\\d+)/', views.download, name='download'),
]
