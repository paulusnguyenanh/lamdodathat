# Generated by Django 3.2.6 on 2021-09-08 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210906_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
    ]