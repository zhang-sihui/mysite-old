from django.urls import path
from . import views

app_name = 'messageboard'

urlpatterns = [
    path('', views.MessageIndexView.as_view(), name='messages'),
    path('addMessage', views.add_message, name='add_message'),
]
