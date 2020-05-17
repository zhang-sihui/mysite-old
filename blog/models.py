import datetime
from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


# Create your models here.
class Article(models.Model):
    title = models.CharField('标题', max_length=200)
    author = models.CharField('作者', max_length=16)
    category = models.CharField('分类', max_length=10, default='其他')
    body = MDTextField('内容')
    pub_date = models.DateTimeField('date published', default=timezone.now)
    views = models.IntegerField('浏览量', default=0)

    def __str__(self):
        return self.title
    """
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    """


class Notice(models.Model):
    caption = models.CharField(max_length=100)
    content = MDTextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.caption
