from django.db import models
from .base import BaseModel
from .project import Project

class Milestone(models.Model):
    """milestones in a project."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestones')
    title = models.CharField(max_length=255)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
