import markdown
from django.shortcuts import render, get_object_or_404
from .models import Watchlist


# Create your views here.

def get_watchlists(request):
    watchlists = Watchlist.objects.all().order_by('-pub_date')
    return render(request, 'watchlist/watchlist.html', locals())


def get_reviews(request, review_id):
    watchlists = get_object_or_404(Watchlist, pk=int(review_id))
    watchlists.content = markdown.markdown(watchlists.content,
                                           extensions=[
                                               "markdown.extensions.extra",
                                               "markdown.extensions.codehilite",
                                               "markdown.extensions.toc",
                                           ])
    return render(request, 'watchlist/review.html', locals())


def get_books(request):
    books = Watchlist.objects.filter(category='book').order_by('-pub_date')
    return render(request, 'watchlist/book_film.html', locals())


def get_films(request):
    films = Watchlist.objects.filter(category='film').order_by('-pub_date')
    return render(request, 'watchlist/book_film.html', locals())
