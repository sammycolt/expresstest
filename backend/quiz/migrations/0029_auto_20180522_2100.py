# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-22 21:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0028_auto_20180522_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizpassing',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 22, 21, 0, 31, 379835)),
        ),
    ]