from django.db import models
from django.utils import timezone


# Create your models here.

class File(models.Model):
    file_name = models.CharField('文件名', max_length=100)
    pub_date = models.DateTimeField('上传日期', default=timezone.now)
    downloads_count = models.IntegerField('下载数', default=0)

    def __str__(self):
        return self.file_name
