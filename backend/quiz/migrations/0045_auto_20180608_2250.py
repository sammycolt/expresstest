# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-08 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0044_universityuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityuser',
            name='avatar',
            field=models.TextField(blank=True),
        ),
    ]