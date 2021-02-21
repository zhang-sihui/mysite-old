from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


# Create your models here.

class Article(models.Model):
    states = (
        ('draft', '草稿'),
        ('pub', '发布'),
    )
    title = models.CharField('文章标题', max_length=200)
    author = models.CharField('作者', max_length=16)
    category = models.CharField('分类', max_length=10, default='其他')
    body = MDTextField('内容')
    pub_date = models.DateTimeField('发布日期', default=timezone.now)
    views = models.IntegerField('浏览量', default=0)
    mod_date = models.DateTimeField('修改时间', default=timezone.now)
    state = models.CharField('状态', max_length=8, choices=states, default='draft')

    def __str__(self):
        return self.title
