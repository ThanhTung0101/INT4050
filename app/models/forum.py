from django.db import models

from .base import BaseModel


class Forum(BaseModel):
    name = models.CharField(default="", blank=True, max_length=255)
    owner = models.ForeignKey(
        "Student",
        on_delete=models.CASCADE,
        related_name="forums",
    )

    def __str__(self) -> str:
        return self.name
