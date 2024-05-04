from django.db import models

from .base import BaseModel


class Connect(BaseModel):
    owner = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        related_name="owner_connects",
    )
    name = models.CharField(max_length=255)
    description = models.TextField(default="", max_length=2048, blank=True)
    subject = models.ForeignKey(
        "Subject",
        on_delete=models.CASCADE,
        related_name="subject_connects",
    )
    people = models.ManyToManyField(
        "Student",
        related_name="people_connects",
        blank=True,
    )
