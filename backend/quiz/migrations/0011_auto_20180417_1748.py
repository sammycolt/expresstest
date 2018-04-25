# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-17 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20180415_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToQuiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.QuizTest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.UniversityUser')),
            ],
        ),
        migrations.AddField(
            model_name='quiztest',
            name='readers',
            field=models.ManyToManyField(through='quiz.UserToQuiz', to='quiz.UniversityUser'),
        ),
    ]