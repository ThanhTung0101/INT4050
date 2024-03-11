from django.db import models

from .group import Group
from .student import Student


class GroupMessage(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="group_messages"
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="group_messages"
    )
    message = models.TextField()

    def __str__(self):
        return f"Message group: {self.message}"
