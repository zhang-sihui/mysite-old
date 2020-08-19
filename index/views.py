import json
import time
import datetime
from django.shortcuts import render
from .models import UserIP


# Create your views here.
# 主页面
def index(request):
    utc_isoformat = time_transform(0 * 60)
    london_isoformat = time_transform(1 * 3600)
    moscow_isoformat = time_transform(3 * 3600)
    beijing_isoformat = time_transform(8 * 3600)
    tokyo_isoformat = time_transform(9 * 3600)
    Newyork_isoformat = time_transform(-4 * 3600)

    ip_msg = UserIP.objects.all()
    length = len(ip_msg)
    user_ip = get_ip(request)
    if user_ip:
        ip = UserIP.objects.filter(user_ip=user_ip)
        if not ip:
            ip_info = UserIP.objects.create()
            ip_info.user_ip = user_ip
            ip_info.serial_number = length+1
            ip_info.save()
        # ip_get = UserIP.objects.get(user_ip=user_ip)
    ip_infos = UserIP.objects.all()
    return render(request, 'index/home.html', locals())


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def time_transform(timedelta):
    timedelta = datetime.timedelta(days=0, seconds=int(timedelta), microseconds=0)
    transform_time = (datetime.datetime.utcnow() + timedelta).isoformat()
    return transform_time[:10] + " " + transform_time[11:19]


# 关于我
def about_me(request):
    return render(request, 'index/about_me.html')
