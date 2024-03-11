from django.db import models

from .post import Post
from .student import Student


class PostDislike(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="post_dislikes"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_dislikes"
    )
