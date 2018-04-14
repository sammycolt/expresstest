from django.db import models
from django.contrib.auth.models import User


USER_CHOICES = (
    ('0', 'Teacher'),
    ('1', 'Student')
)

class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UniversityUser(models.Model):
    user = models.OneToOneField(User)
    type = models.CharField(max_length=1, choices=USER_CHOICES)


class QuizTest(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User)

class QuizAnswer(models.Model):
    text = models.TextField()
    is_correct = models.NullBooleanField()

class AnswerByUser(models.Model):
    user = models.ForeignKey(UniversityUser)
    answer = models.ForeignKey(QuizAnswer)

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(QuizTest, related_name='questions')
    text = models.TextField()
    answers = models.ManyToManyField(QuizAnswer, blank=True)