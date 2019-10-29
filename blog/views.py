from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def programming(request):
    return render(request, 'blog/programming.html')


def thinking(request):
    return render(request, 'blog/thinking.html')


def other(request):
    return render(request, 'blog/other.html')
