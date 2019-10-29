from django.urls import path, re_path
from . import views
from . import views as test

app_name = 'polls'

urlpatterns = [
    # main
    path('', views.home, name='home'),
    # polls
    path('vote/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # files
    path('upload/', views.upload, name='upload'),
    path('uploaded/', views.uploaded, name='uploaded'),
    path('show/', views.show, name='show'),
    re_path('download/(?P<id>\\d+)', views.download, name='download'),
    # interest
    path('image/', views.image, name='image'),
    path('music/', views.music, name='music'),
    path('film/', views.film, name='film'),
]
# error
handler404 = test.page_not_founds
handler500 = test.server_error
