from django.db import models

from .post import Post
from .student import Student


class PostLike(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="post_likes"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_likes"
    )
