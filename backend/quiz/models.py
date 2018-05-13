from django.db import models
from django.contrib.auth.models import User


USER_CHOICES = (
    ('0', 'Teacher'),
    ('1', 'Student')
)

QUESTION_TYPE_CHOICES = (
    ('0', 'ManyAnswers'),
    ('1', 'OneAnswer'),
    ('2', 'OpenAnswer')
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
    readers = models.ManyToManyField(User, through='UserToQuiz', related_name='quiz')
    groups_of_readers = models.ManyToManyField('Group', through='QuizToGroup', related_name='quiz')
    courses = models.ManyToManyField('Course', through='QuizToCourse', related_name='quiz')

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

class AnswerToQuestion(models.Model):
    answer = models.ForeignKey(QuizAnswer, related_name='questions')
    question = models.ForeignKey(QuizQuestion)

class QuizResults(models.Model):
    user = models.ForeignKey(User)
    quiz = models.ForeignKey(QuizTest)
    correct_questions = models.ManyToManyField(QuizQuestion, through='QuestionToResult')
    total_score = models.FloatField()
    percentage = models.FloatField(default=0)

class QuestionToResult(models.Model):
    question = models.ForeignKey(QuizQuestion)
    result = models.ForeignKey(QuizResults)

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

