from django.shortcuts import render


# Create your views here.

# 网站主页面
def index(request):
    return render(request, 'index/home.html')
