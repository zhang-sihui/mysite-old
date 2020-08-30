import datetime
import markdown
from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.

def blog(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'blog/blog.html', locals())


def blog_body(request, blog_id):
    article = get_object_or_404(Article, pk=int(blog_id))
    article.body = markdown.markdown(article.body.replace('\r\n', '\n'),
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    article.views += 1
    article.save()
    return render(request, 'blog/blog_body.html', locals())


def search_blogs(request):
    q = request.GET.get('q')
    articles = Article.objects.all().order_by('-pub_date')
    articles_part = articles[:10]
    search_articles = Article.objects.filter(title__icontains=q)
    search_articles_count = len(search_articles)
    success_search_msg = '{} 个 {} 相关内容。'.format(search_articles_count, q)
    not_search_msg = '没有与 {} 相关的内容。'.format(q)
    return render(request, 'blog/search_blogs.html', locals())


def display_labels(request):
    labels = Article.objects.values_list('category')
    labels_list = set(labels)
    labels_set = {str(label)[2:-3] for label in labels_list}
    return render(request, 'blog/display_labels.html', locals())


def get_blogs_by_label(request, label):
    blog_label = Article.objects.filter(category=label)
    return render(request, 'blog/blogs_by_label.html', locals())


def display_years(request):
    current_year = datetime.datetime.now().year
    years = set()
    for i in range(2018, current_year + 1):
        years.add(i)
    return render(request, 'blog/display_years.html', locals())


def get_blogs_by_year(request, year):
    articles = Article.objects.filter(pub_date__year=year)
    return render(request, 'blog/blogs_by_year.html', locals())
