# Generated by Django 2.1.3 on 2020-05-18 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0003_delete_messageboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.CharField(max_length=20, verbose_name='用户ip')),
                ('access_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='首次访问时间')),
            ],
        ),
    ]