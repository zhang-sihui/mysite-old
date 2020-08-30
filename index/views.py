import datetime
from django.shortcuts import render
from .models import UserIP


# Create your views here.

def index(request):
    UTC_isoformat = utc_to_iso(0 * 60)
    London_isoformat = utc_to_iso(1 * 3600)
    Moscow_isoformat = utc_to_iso(3 * 3600)
    Beijing_isoformat = utc_to_iso(8 * 3600)
    Tokyo_isoformat = utc_to_iso(9 * 3600)
    NewYork_isoformat = utc_to_iso(-4 * 3600)

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
    return render(request, 'index/index.html', locals())


def utc_to_iso(timedelta):
    timedelta = datetime.timedelta(days=0, seconds=int(timedelta), microseconds=0)
    iso_time = (datetime.datetime.utcnow() + timedelta).isoformat()
    return iso_time[:10] + " " + iso_time[11:19]


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def about_me(request):
    return render(request, 'index/about_me.html')
