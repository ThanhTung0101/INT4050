from django.db import models

from app.models import Post, Student


class Forum(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="forums"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="forums"
    )
