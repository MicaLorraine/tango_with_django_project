# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-09 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20170910_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='likes',
        ),
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='category',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
