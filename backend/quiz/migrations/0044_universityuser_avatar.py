# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0043_quizquestion_text_in_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='universityuser',
            name='avatar',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]