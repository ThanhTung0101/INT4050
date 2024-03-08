from django.db import models

from .post import Post
from .student import Student


class DisLikePost(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="dislike_posts"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="dislike_posts"
    )
