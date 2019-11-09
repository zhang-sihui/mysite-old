import markdown
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article


# Create your views here.


def index(request):
    contexts = Article.objects.all().order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'contexts': contexts})


def blog_list(request, id):
    context = get_object_or_404(Article, pk=int(id))
    context.body = markdown.markdown(context.body.replace("\r\n", '  \n'),
                                     extensions=[
                                         "markdown.extensions.extra",
                                         "markdown.extensions.codehilite",
                                         "markdown.extensions.toc",
                                     ])
    return render(request, 'blog/blog_list.html', {'context': context})


def programming(request):
    context = Article.objects.filter(category='programming').order_by('-pub_date')[:5]
    return render(request, 'blog/programming.html', {'context': context})


def thinking(request):
    context = Article.objects.filter(category='thinking').order_by('-pub_date')[:5]
    return render(request, 'blog/thinking.html', {'context': context})


def other(request):
    contexts = Article.objects.filter(category='other').order_by('-pub_date')[:5]
    return render(request, 'blog/other.html', {'contexts': contexts})


def search(request):
    q = request.GET.get('q')
    contexts = Article.objects.all().order_by('-pub_date')[:5]
    search_list = Article.objects.filter(title__icontains=q)
    error_msg = 'No result'
    return render(request, 'blog/search.html', {'search_list': search_list,
                                                'error_msg': error_msg,
                                                'contexts': contexts})
