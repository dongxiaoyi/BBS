# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(related_name='_userprofile_friends_+', to='web.UserProfile'),
        ),
    ]
