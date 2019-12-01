from django.shortcuts import render


# Create your views here.

# 主页面
def index(request):
    return render(request, 'index/home.html')
