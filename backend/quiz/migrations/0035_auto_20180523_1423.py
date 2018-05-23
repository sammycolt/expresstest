# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-23 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0034_auto_20180523_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiztest',
            name='num_of_winners',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='quiztest',
            name='scoring_system',
            field=models.CharField(choices=[('0', 'For everyone'), ('1', 'For firsts')], default='0', max_length=1),
        ),
    ]
