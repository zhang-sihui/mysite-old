from django.urls import path, re_path
from . import views


app_name = 'polls'

urlpatterns = [
    # polls/
    path('vote/', views.IndexView.as_view(), name='vote'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # files
    path('upload/', views.upload, name='upload'),
    path('uploaded/', views.uploaded, name='uploaded'),
    path('show/', views.show, name='show'),
    re_path('download/(?P<file_id>\\d+)/', views.download, name='download'),
    # interest
    path('music/', views.music, name='music'),

]

