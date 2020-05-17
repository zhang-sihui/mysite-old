import markdown
from django.shortcuts import render, get_object_or_404
from .models import Article


# Create your views here.

# 博客总页面
def blog(request):
    contexts = Article.objects.all().order_by('-pub_date')
    contexts_part = contexts[:10]
    return render(request, 'blog/blog.html', locals())


# 博客具体内容
def blog_body(request, blog_id):
    context = get_object_or_404(Article, pk=int(blog_id))
    context.body = markdown.markdown(context.body.replace('\r\n', '\n'),
                                     extensions=[
                                         "markdown.extensions.extra",
                                         "markdown.extensions.codehilite",
                                         "markdown.extensions.toc",
                                     ])
    context.views += 1
    context.save()
    return render(request, 'blog/blog_body.html', locals())


# 博客搜索功能
def search(request):
    q = request.GET.get('q')  # 获取搜索表单关键词
    contexts = Article.objects.all().order_by('-pub_date')
    contexts_part = contexts[:10]
    search_list = Article.objects.filter(title__icontains=q)  # 查询标题中含有关键词的博客
    search_count = len(search_list)
    success_msg = '{} results for {}'.format(search_count, q)
    error_msg = '0 results for {}'.format(q)
    return render(request, 'blog/search.html', locals())


# 展示所有标签,去除相同标签
def display_label(request):
    labels = Article.objects.values_list('category')
    labels_list = set(labels)
    labels_set = {str(label)[2:-3] for label in labels_list}
    return render(request, 'blog/display_label.html', locals())


# 根据标签值获取同标签文章
def get_blog_by_label(request, label):
    blog_label = Article.objects.filter(category=label)
    return render(request, 'blog/blog_by_label.html', locals())
