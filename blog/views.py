import markdown
from django.shortcuts import render, get_object_or_404
from .models import Article, Notice


# Create your views here.

# 博客总页面
def blog(request):
    notices = Notice.objects.all()
    contexts = Article.objects.all().order_by('-pub_date')[:15]
    return render(request, 'blog/blog.html', locals())


# 博客具体内容
def blog_body(request, blog_id):
    context = get_object_or_404(Article, pk=int(blog_id))
    context.body = markdown.markdown(context.body.replace("\r\n", '  \n'),
                                     extensions=[
                                         "markdown.extensions.extra",
                                         "markdown.extensions.codehilite",
                                         "markdown.extensions.toc",
                                     ])
    return render(request, 'blog/blog_body.html', locals())


# 获取关于编程分类的博客
def programming(request):
    context = Article.objects.filter(category='programming').order_by('-pub_date')[:15]
    return render(request, 'blog/programming.html', locals())


# 获取关于thinking分类的博客
def thinking(request):
    context = Article.objects.filter(category='thinking').order_by('-pub_date')[:15]
    return render(request, 'blog/thinking.html', locals())


# 获取关于other分类的博客
def other(request):
    contexts = Article.objects.filter(category='other').order_by('-pub_date')[:15]
    return render(request, 'blog/other.html', locals())


# 博客搜索功能
def search(request):
    q = request.GET.get('q')  # 获取搜索表单关键词
    contexts = Article.objects.all().order_by('-pub_date')[:15]
    notices = Notice.objects.all()
    search_list = Article.objects.filter(title__icontains=q)  # 查询标题中含有关键词的博客
    search_count = len(search_list)
    success_msg = '{} results for {}'.format(search_count, q)
    error_msg = '0 results for {}'.format(q)
    return render(request, 'blog/search.html', locals())
