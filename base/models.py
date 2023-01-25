from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from todo_list import settings

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    task = models.TextField(max_length=100)
    complete = models.BooleanField(default=False)
    deadline = models.DateField()
    timestamp = models.DateField(default=datetime.now())

    def __str__(self):
        return self.task

    #odering
    class Meta:
        ordering = ['complete']



