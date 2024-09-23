from django.db import models
from .base import BaseModel
from .milestone import Milestone

class Task(models.Model):
    """tasks in a milestone."""
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
