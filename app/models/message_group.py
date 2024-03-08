from django.db import models

from app.models import Student

from .group import Group


class MessageGroup(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="messages_group"
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="messages_group"
    )
    message = models.TextField()
