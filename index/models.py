from django.db import models
from django.utils import timezone


# Create your models here.


class UserIP(models.Model):
    user_ip = models.CharField('用户ip', max_length=20)
    access_time = models.DateTimeField('首次访问时间', default=timezone.now)
    serial_number = models.CharField('访问序号', max_length=10, default=0)
    ip_attribution = models.CharField('ip地址', max_length=64, default='')
