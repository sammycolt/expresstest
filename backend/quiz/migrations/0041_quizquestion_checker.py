# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-25 11:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0040_auto_20180525_0812'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizquestion',
            name='checker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Checker'),
        ),
    ]
