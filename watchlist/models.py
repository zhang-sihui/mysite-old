from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


# Create your models here.

class Watchlist(models.Model):
    cate = (
        ('film', '电影'),
        ('book', '书籍'),
    )
    title = models.CharField('标题', max_length=128)
    category = models.CharField('分类', max_length=32, choices=cate)
    pub_date = models.DateTimeField('发布日期', default=timezone.now)
    content = MDTextField('观看感想')

    def __str__(self):
        return self.title
