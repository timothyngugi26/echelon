from django.db import models
from django.contrib.auth.models import User
from .base import BaseModel
from django.conf import settings
from echelon.settings import *

class Project(models.Model):
    """Model Representing a project."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
