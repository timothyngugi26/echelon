from django.db import models
from .base import BaseModel
from .project import Project

class Milestone(BaseModel):
    """milestones in a project."""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='milestones')
    due_date = models.DateField()
