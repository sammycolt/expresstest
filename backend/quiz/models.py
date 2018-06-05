from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
import pytz
from django.dispatch import receiver
import os
from django.contrib.sites.models import Site


USER_CHOICES = (
    ('0', 'Teacher'),
    ('1', 'Student')
)

QUESTION_TYPE_CHOICES = (
    ('0', 'ManyAnswers'),
    ('1', 'OneAnswer'),
    ('2', 'OpenAnswer')
)


SCORING_SYSTEM_CHOICES = (
    ('0', 'For everyone'),
    ('1', 'For first')
)

class Checker(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    file = models.FileField(blank=False, null=False, upload_to='./quiz/checkers')
    author = models.ForeignKey(User, null=True)

    @property
    def filename(self):
        return self.file.path.split('/')[-1]

    @property
    def file_url(self):
        filename = self.file.path.split('/')[-1]
        return 'http://localhost:8000/quiz/checkers/' + filename


@receiver(models.signals.post_delete, sender=Checker)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

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
    max_time = models.IntegerField(default=2)
    max_attempts = models.IntegerField(default=3)
    readers = models.ManyToManyField(User, through='UserToQuiz', related_name='quiz')
    groups_of_readers = models.ManyToManyField('Group', through='QuizToGroup', related_name='quiz')
    courses = models.ManyToManyField('Course', through='QuizToCourse', related_name='quiz')
    scoring_system = models.CharField(max_length=1, choices=SCORING_SYSTEM_CHOICES, default='0')
    num_of_winners = models.IntegerField(default=1, blank=True)

class UserToQuiz(models.Model):
    quiz = models.ForeignKey(QuizTest)
    user = models.ForeignKey(User)

class QuizAnswer(models.Model):
    answer_text = models.TextField()
    is_correct = models.NullBooleanField()

class AnswerByUser(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey(QuizAnswer)

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(QuizTest, related_name='questions')
    text = models.TextField()
    answers = models.ManyToManyField(QuizAnswer, through='AnswerToQuestion')
    score = models.IntegerField(default=1)
    type = models.CharField(max_length=1, choices=QUESTION_TYPE_CHOICES, default='0')
    use_checker = models.BooleanField(blank=True, default=False)
    checker = models.ForeignKey(Checker, blank=True, null=True)
    text_in_html = models.BooleanField(blank=True, default=False)

class AnswerToQuestion(models.Model):
    answer = models.ForeignKey(QuizAnswer, related_name='questions')
    question = models.ForeignKey(QuizQuestion)

class QuizResults(models.Model):
    # user = models.ForeignKey(User)
    # quiz = models.ForeignKey(QuizTest)
    # passing = models.ForeignKey(QuizPassing)
    correct_questions = models.ManyToManyField(QuizQuestion, through='QuestionToResult')
    total_score = models.FloatField(default=0)
    percentage = models.FloatField(default=0)

class QuestionToResult(models.Model):
    question = models.ForeignKey(QuizQuestion)
    result = models.ForeignKey(QuizResults, related_name='questions')
    show_in_res = models.BooleanField(default=True)

class Group(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User, through='UserToGroup')

    def __str__(self):
        return self.name

class UserToGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)

    def __str__(self):
        return self.user.username + ' -> ' + self.group.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group, through='GroupToCourse')

    def __str__(self):
        return self.name

class GroupToCourse(models.Model):
    group = models.ForeignKey(Group)
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.group.name + '->' + self.course.name

class QuizToCourse(models.Model):
    quiz = models.ForeignKey(QuizTest)
    course = models.ForeignKey(Course)

class QuizToGroup(models.Model):
    quiz = models.ForeignKey(QuizTest)
    group = models.ForeignKey(Group)

class QuizPassing(models.Model):
    quiz = models.ForeignKey(QuizTest)
    user = models.ForeignKey(User)
    answers = models.ManyToManyField(QuizAnswer, through='AnswerToPassing')
    result = models.ForeignKey(QuizResults, related_name='passing')
    start_time = models.DateTimeField()
    duration = models.IntegerField()  # in minutes
    end_time = models.DateTimeField(default=datetime.now, blank=False)
    attempt = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print('!?!', self.end_time)
        super().save(force_insert, force_update, using, update_fields)

    @property
    def remaining_time(self):
        # print(type(self.end_time))
        # print(type(self.start_time))
        # print(self.end_time)
        # timediff = -1
        timediff = self.end_time.replace(tzinfo=pytz.UTC) - self.start_time.replace(tzinfo=pytz.UTC)
        if timediff.total_seconds() < 0:
            # print('ahkbshbahj')
            return -1
        else:
            return timediff.total_seconds()

    @property
    def remaining_attempts(self):
        return self.quiz.max_attempts - self.attempt

    @property
    def is_going(self):
        now = timezone.now().replace(tzinfo=pytz.UTC)
        timediff = now - self.start_time.replace(tzinfo=pytz.UTC)
        timediff_in_minutes = timediff.total_seconds() / 60

        timediff2 = now - self.end_time.replace(tzinfo=pytz.UTC)

        return not(timediff_in_minutes > self.duration or timediff2.total_seconds() > 0)

    @property
    def seconds_per_end(self):
        now = timezone.now().replace(tzinfo=pytz.UTC)
        timediff = now - self.start_time.replace(tzinfo=pytz.UTC)
        ans = 60 * self.duration - timediff.total_seconds()
        if ans > 0 and self.is_going:
            return ans
        else:
            return 0

class AnswerToPassing(models.Model):
    answer = models.ForeignKey(QuizAnswer)
    passing = models.ForeignKey(QuizPassing)

