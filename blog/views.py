import datetime
import markdown
from django.shortcuts import render, get_object_or_404
from django.db.models import Min, Max
from .models import Article


# Create your views here.

def get_label_and_year_to_articles():
    labels_QuerySet = Article.objects.values_list('category').filter(state='pub')
    labels_set = {str(label)[2:-3] for label in set(labels_QuerySet)}
    label_to_articles = {}
    for label_set in labels_set:
        articles_by_label = Article.objects.filter(category=label_set, state='pub')
        label_to_articles[label_set] = articles_by_label

    min_pub_date = Article.objects.aggregate(Min('pub_date'))['pub_date__min']
    min_pub_date_year = min_pub_date.year if min_pub_date else datetime.datetime.now().year
    max_pub_date = Article.objects.aggregate(Max('pub_date'))['pub_date__max']
    max_pub_date_year = max_pub_date.year if max_pub_date else datetime.datetime.now().year

    years_set = set()
    for i in range(min_pub_date_year, max_pub_date_year + 1):
        years_set.add(i)
    year_to_articles = {}
    for year_set in years_set:
        articles_by_year = Article.objects.filter(pub_date__year=year_set, state='pub')
        if articles_by_year:
            year_to_articles[year_set] = articles_by_year
    return label_to_articles, year_to_articles


def article(request):
    articles = Article.objects.filter(state='pub').order_by('-pub_date')
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/article.html', locals())


def article_body(request, article_id):
    article = get_object_or_404(Article, pk=int(article_id))
    article.views += 1
    article.save()
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/article_body.html', locals())


def get_search_articles(request):
    q = request.GET.get('q')
    articles = Article.objects.all().filter(state='pub').order_by('-pub_date')
    search_articles = Article.objects.filter(title__icontains=q, state='pub')
    search_articles_count = len(search_articles)
    success_search_msg = '{} results for {}'.format(search_articles_count, q)
    not_search_msg = 'No {} '.format(q)
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/search_articles.html', locals())


def get_articles_by_label(request, label):
    article_label = Article.objects.filter(category=label, state='pub')
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/articles_by_label.html', locals())


def get_articles_by_year(request, year):
    articles = Article.objects.filter(pub_date__year=year, state='pub')
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/articles_by_year.html', locals())
