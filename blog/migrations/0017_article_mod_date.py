# Generated by Django 2.2 on 2020-10-17 09:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_delete_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='mod_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
    ]