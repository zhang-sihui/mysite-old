import datetime
import markdown
from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.
def get_label_and_year_to_articles():
    labels_QuerySet = Article.objects.values_list('category')
    labels_set = {str(label)[2:-3] for label in set(labels_QuerySet)}
    label_to_articles = {}
    for label_set in labels_set:
        articles_by_label = Article.objects.filter(category=label_set)
        label_to_articles[label_set] = articles_by_label

    current_year = datetime.datetime.now().year
    years_set = set()
    for i in range(2019, current_year + 1):
        years_set.add(i)
    year_to_articles = {}
    for year_set in years_set:
        articles_by_year = Article.objects.filter(pub_date__year=year_set)
        year_to_articles[year_set] = articles_by_year
    return label_to_articles, year_to_articles


def blog(request):
    articles = Article.objects.all().order_by('-pub_date')
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/blog.html', locals())


def blog_body(request, blog_id):
    article = get_object_or_404(Article, pk=int(blog_id))
    article.views += 1
    article.save()
    article.body = markdown.markdown(article.body,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/blog_body.html', locals())


def search_blogs(request):
    q = request.GET.get('q')
    articles = Article.objects.all().order_by('-pub_date')
    articles_part = articles[:10]
    search_articles = Article.objects.filter(title__icontains=q)
    search_articles_count = len(search_articles)
    success_search_msg = '{} 个 {} 相关内容。'.format(search_articles_count, q)
    not_search_msg = '没有与 {} 相关的内容。'.format(q)
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/search_blogs.html', locals())


def get_blogs_by_label(request, label):
    blog_label = Article.objects.filter(category=label)
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/blogs_by_label.html', locals())


def get_blogs_by_year(request, year):
    articles = Article.objects.filter(pub_date__year=year)
    label_to_articles, year_to_articles = get_label_and_year_to_articles()
    return render(request, 'blog/blogs_by_year.html', locals())
