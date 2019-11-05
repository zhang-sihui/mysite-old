from django.db import models
from mdeditor.fields import MDTextField
from django.utils import timezone
import datetime
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default='programming')
    body = MDTextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
