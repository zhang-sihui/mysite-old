from django.db import models
from django.utils import timezone


# Create your models here.


class MessageBoard(models.Model):
    message = models.TextField(max_length=1024)
    sub_date = models.DateTimeField(default=timezone.now)
    reply = models.TextField(max_length=1024, default="暂未回复")

    def __str__(self):
        return self.message
