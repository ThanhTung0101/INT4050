from django.db import models

from .base import BaseModel


class Document(BaseModel):
    name = models.CharField(default="", max_length=255, blank=True)
    file = models.FileField(upload_to="documents/")
    description = models.TextField(default="", max_length=1000, blank=True)
    owner = models.ForeignKey(
        "Student", on_delete=models.CASCADE, related_name="documents"
    )

    def __str__(self):
        return f"{self.name}"
