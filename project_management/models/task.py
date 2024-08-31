from django.db import models
from .base import BaseModel
from .milestone import Milestone

class Task(BaseModel):
    """tasks in a milestone."""
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, related_name='tasks')
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
