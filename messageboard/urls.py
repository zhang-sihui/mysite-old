from django.urls import path
from . import views

app_name = 'messageboard'

urlpatterns = [
    path('', views.MsgBoardIndexView.as_view(), name='messages'),
    path('create', views.create_message, name='create_message'),
]
