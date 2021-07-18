from django.db import models
from django.utils import timezone


# Create your models here.

class MessageBoard(models.Model):
    username = models.CharField('匿名', max_length=16, default='')
    content = models.TextField('内容', max_length=1024)
    sub_date = models.DateTimeField('日期', default=timezone.now)
    reply = models.TextField('回复内容', max_length=1024, default='暂未回复')
    reply_date = models.DateTimeField('回复日期', default=timezone.now)

    def __str__(self):
        return self.content
