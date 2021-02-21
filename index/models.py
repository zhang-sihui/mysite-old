from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


# Create your models here.

class UserIP(models.Model):
    user_ip = models.CharField('用户ip', max_length=20)
    access_time = models.DateTimeField('首次访问时间', default=timezone.now)
    serial_number = models.CharField('访问序号', max_length=10, default=0)
    ip_attribution = models.CharField('ip地址', max_length=64, default='')


class EverydayVisit(models.Model):
    date = models.DateField('日期', default=timezone.localdate)
    visits = models.IntegerField('访问量', default=0)


class AboutSite(models.Model):
    title = models.CharField('标题', max_length=20)
    pub_date = models.DateTimeField('发布时间', default=timezone.now)
    content = MDTextField('内容')
