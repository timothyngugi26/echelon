from django.db import models
from .base import BaseModel
from .project import Project

class Milestone(models.Model):
    """milestones in a project."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
