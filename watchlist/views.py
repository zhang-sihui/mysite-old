import markdown
from django.shortcuts import render, get_object_or_404
from .models import Checklist


# Create your views here.


# 清单
def watchlist(request):
    checklists = Checklist.objects.all().order_by('-pub_date')
    return render(request, 'watchlist/watchlist.html', locals())


def check_body(request, check_id):
    checklists = get_object_or_404(Checklist, pk=int(check_id))
    checklists.content = markdown.markdown(checklists.content,
                                           extensions=[
                                               "markdown.extensions.extra",
                                               "markdown.extensions.codehilite",
                                               "markdown.extensions.toc",
                                           ])
    return render(request, 'watchlist/check_body.html', locals())


def book(request):
    books = Checklist.objects.filter(category='book').order_by('-pub_date')
    return render(request, 'watchlist/book_film.html', locals())


def film(request):
    films = Checklist.objects.filter(category='film').order_by('-pub_date')
    return render(request, 'watchlist/book_film.html', locals())


# 搜索
def search(request):
    q = request.GET.get('q')
    checklists = Checklist.objects.all().order_by('-pub_date')
    search_list = Checklist.objects.filter(title__icontains=q)
    search_count = len(search_list)
    success_msg = '{} results for {}'.format(search_count, q)
    error_msg = '0 results for {}'.format(q)
    return render(request, 'watchlist/search.html', locals())
