import json
import urllib.request
import markdown
from django.utils import timezone
from django.shortcuts import render
from django.db.models import Sum
from .models import UserIP, EverydayVisit, AboutSite


# Create your views here.

def index(request):
    localtime = timezone.now()
    ips = UserIP.objects.all()
    length = len(ips)
    user_ip = get_user_ip(request)
    if user_ip:
        ip = UserIP.objects.filter(user_ip=user_ip)
        if not ip:
            ip_attribution = get_ip_attribution(user_ip)
            ip_info = UserIP.objects.create()
            ip_info.user_ip = user_ip
            ip_info.serial_number = length+1
            ip_info.ip_attribution = ip_attribution
            ip_info.save()

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

def get_ip_attribution(ip):
    apikey = '588481dc94e6ddc00d10947d57aa8e91'
    url = "http://api.tianapi.com/txapi/ipquery/index?key={}&ip={}".format(apikey, ip)
    req = urllib.request.urlopen(url)
    content = req.read().decode('utf-8')
    jsonResponse = json.loads(content)  # 将数据转化为 json 格式
    country, province, city, district, isp = '', '', '', '', ''
    if jsonResponse['code'] == 200:
        newslist = jsonResponse['newslist']
        country = newslist[0]['country'] if newslist[0]['country'] else ''
        province = newslist[0]['province'] if newslist[0]['province'] else ''
        city = newslist[0]['city'] if newslist[0]['city'] else ''
        district = newslist[0]['district'] if newslist[0]['district'] else ''
        isp = newslist[0]['isp'] if newslist[0]['isp'] else ''
    return (country + ' ' + province + ' ' + city + ' ' + district + ' ' + isp)

def about_site(request):
    # 返回日期最近的一条
    about_site = AboutSite.objects.order_by('-pub_date')
    if about_site:
        about_site = about_site[0]
        about_site.content = markdown.markdown(about_site.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    return render(request, 'index/about_site.html', locals())
