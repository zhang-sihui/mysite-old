# Generated by Django 2.1.3 on 2019-10-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191030_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='body',
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]