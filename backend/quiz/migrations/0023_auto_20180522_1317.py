# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-22 13:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0022_auto_20180521_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztest',
            name='max_time',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='quizpassing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 22, 13, 17, 3, 387794, tzinfo=utc)),
        ),
    ]
