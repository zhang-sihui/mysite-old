from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


# Create your models here.

class Checklist(models.Model):
    cate = (
        ('film', '电影'),
        ('book', '书籍'),
    )
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=32, choices=cate)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    content = MDTextField()

    def __str__(self):
        return self.title
