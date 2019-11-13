import datetime
from django.utils import timezone
from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.create_time <= now

    was_created_recently.admin_order_field = 'create_time'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'
