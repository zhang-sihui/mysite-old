# Generated by Django 2.1.3 on 2020-04-21 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20191124_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['pub_date']},
        ),
    ]