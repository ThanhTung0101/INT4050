from django.db import models

from app.models import Student


class Forum(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="forums"
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
