from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    """Consists of common attributes and methods."""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """defines BaseModel as an abstract base class."""
        abstract = True

    def __str__(self):
        """Return a string represetation of the model instance.
        Returns:
            str: The value of the `name` field.
        """
        return self.name
