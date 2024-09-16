from django.db import models
from .base import BaseModel
from .milestone import Milestone

class Task(models.Model):
    """tasks in a milestone."""
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()

    def __str__(self):
        return self.title
