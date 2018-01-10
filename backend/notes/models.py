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

    #CustomFields
    type = models.CharField(max_length=1, choices=USER_CHOICES)
