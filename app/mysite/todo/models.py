import datetime

from django.utils import timezone
from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    limit_date = models.DateTimeField()

    def __str__(self):
        return self.title
