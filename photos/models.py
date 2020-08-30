from django.db import models
from django.utils import timezone


# Create your models here.

class Photo(models.Model):
    photo_name = models.CharField('图片名称', max_length=128)
    pub_date = models.DateTimeField('上传日期', default=timezone.now)

    def __str__(self):
        return self.photo_name
