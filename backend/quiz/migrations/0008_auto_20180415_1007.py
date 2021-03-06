# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-15 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20180414_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerToQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.QuizAnswer')),
            ],
        ),
        migrations.AlterModelOptions(
            name='quizquestion',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='quizquestion',
            unique_together=set([]),
        ),
        migrations.AddField(
            model_name='answertoquestion',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.QuizQuestion'),
        ),
        migrations.RemoveField(
            model_name='quizquestion',
            name='answers',
        ),
    ]
