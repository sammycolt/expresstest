# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-19 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0013_auto_20180419_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionToResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.QuizQuestion')),
            ],
        ),
        migrations.RemoveField(
            model_name='answertoresult',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='answertoresult',
            name='result',
        ),
        migrations.RemoveField(
            model_name='quizresults',
            name='correct_answers',
        ),
        migrations.DeleteModel(
            name='AnswerToResult',
        ),
        migrations.AddField(
            model_name='questiontoresult',
            name='result',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.QuizResults'),
        ),
        migrations.AddField(
            model_name='quizresults',
            name='correct_questions',
            field=models.ManyToManyField(through='notes.QuestionToResult', to='notes.QuizQuestion'),
        ),
    ]
