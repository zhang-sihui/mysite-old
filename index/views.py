from django.utils import timezone
from django.shortcuts import render
from django.db.models import Sum
from .models import UserIP, EverydayVisit


# Create your views here.

def index(request):
    localtime = timezone.now()

    ips = UserIP.objects.all()
    length = len(ips)
    user_ip = get_user_ip(request)
    if user_ip:
        ip = UserIP.objects.filter(user_ip=user_ip)
        if not ip:
            ip_info = UserIP.objects.create()
            ip_info.user_ip = user_ip
            ip_info.serial_number = length+1
            ip_info.save()
    ips_info = UserIP.objects.all()

    today_visits = EverydayVisit.objects.filter(date=timezone.localdate())
    if not today_visits:
        today_visits = EverydayVisit.objects.create()
    today_visits = EverydayVisit.objects.get(date=timezone.localdate())
    today_visits.visits += 1
    today_visits.save()
    total_visits = EverydayVisit.objects.aggregate(Sum('visits'))
    return render(request, 'index/index.html', locals())


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def about_me(request):
    return render(request, 'index/about_me.html')
