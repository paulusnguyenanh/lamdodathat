# Generated by Django 3.2.7 on 2021-09-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210917_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=0, unique=True),
            preserve_default=False,
        ),
    ]