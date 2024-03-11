from django.db import models

from .post import Post
from .student import Student


class PostTag(models.Model):
    admin = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="post_tags"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_tags"
    )
    name = models.CharField(max_length=255)
    background_color = models.CharField(max_length=100)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return f"Subject learn: {self.name}"
