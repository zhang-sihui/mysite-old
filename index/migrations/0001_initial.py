# Generated by Django 2.1.3 on 2019-11-30 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1024)),
                ('sub_data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]