# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 07:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_article_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
