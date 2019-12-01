from django.urls import path
from . import views


app_name = 'messageboard'

urlpatterns = [

    path('message_list/', views.MsgBoardIndexView.as_view(), name='message_list'),
    path('message_create/', views.MsgBoardCreateView.as_view(), name='message_create'),
]
