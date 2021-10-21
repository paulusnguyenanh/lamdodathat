# Generated by Django 3.2.7 on 2021-09-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, null=True, unique=True),
        ),
    ]