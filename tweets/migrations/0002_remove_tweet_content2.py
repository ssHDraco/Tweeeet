# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-23 09:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='content2',
        ),
    ]
