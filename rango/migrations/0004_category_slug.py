# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20160817_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
    ]