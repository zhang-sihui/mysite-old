from django.urls import path
from . import views


app_name = 'messageboard'

urlpatterns = [
    path('', views.MsgBoardIndexView.as_view(), name='message_list'),
    path('create', views.message_create, name='message_create'),
]
