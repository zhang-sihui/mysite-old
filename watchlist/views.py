import markdown
from django.shortcuts import render, get_object_or_404
from .models import Checklist


# Create your views here.

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


def get_books(request):
    books = Checklist.objects.filter(category='book').order_by('-pub_date')
    return render(request, 'watchlist/book_film.html', locals())


def get_films(request):
    films = Checklist.objects.filter(category='film').order_by('-pub_date')
    return render(request, 'watchlist/book_film.html', locals())


def search_check(request):
    q = request.GET.get('q')
    checklists = Checklist.objects.all().order_by('-pub_date')
    search_list = Checklist.objects.filter(title__icontains=q)
    search_count = len(search_list)
    success_search_msg = '{} 个 {} 相关内容。'.format(search_count, q)
    not_search_msg = '没有与 {} 相关的内容。'.format(q)
    return render(request, 'watchlist/search.html', locals())
