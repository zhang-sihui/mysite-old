# Generated by Django 2.1.3 on 2020-04-20 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200420_1341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='notice',
            new_name='title',
        ),
    ]