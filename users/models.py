from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


# Create your models here.

class User(models.Model):
    username = models.CharField('用户名', max_length=16, unique=True)
    password = models.CharField('密码', max_length=16)
    email = models.EmailField('邮箱', unique=True)
    create_time = models.DateTimeField('注册时间', auto_now_add=True)
    register_code = models.CharField('注册码', max_length=8)  # 注册码

    def __str__(self):
        return self.username


class Notice(models.Model):
    title = models.CharField('通知标题', max_length=200)
    content = MDTextField('通知内容')
    pub_date = models.DateTimeField('通知发布日期', default=timezone.now)

    def __str__(self):
        return self.title
