from django.db import models
from django.contrib.auth.models import User
from .base import BaseModel
from django.conf import settings

# Importing settings
from echelon.settings import *

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
