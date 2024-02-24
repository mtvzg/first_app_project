from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Username(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    login_data = models.DateTimeField(default=timezone.now)
