import json
import time
import datetime
from django.shortcuts import render


# Create your views here.

# 主页面
def index(request):
    utc_isoformat = time_transform(0 * 60)
    london_isoformat = time_transform(1 * 3600)
    moscow_isoformat = time_transform(3 * 3600)
    beijing_isoformat = time_transform(8 * 3600)
    tokyo_isoformat = time_transform(9 * 3600)
    Newyork_isoformat = time_transform(-4 * 3600)
    return render(request, 'index/home.html', locals())


def time_transform(timedelta):
    timedelta = datetime.timedelta(days=0, seconds=int(timedelta), microseconds=0)
    transform_time = (datetime.datetime.utcnow() + timedelta).isoformat()
    return transform_time[:10] + " " + transform_time[11:19]


# 关于我
def about_me(request):
    return render(request, 'index/about_me.html')




