# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0042_quizquestion_use_checker'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='text_in_html',
            field=models.BooleanField(default=False),
        ),
    ]
