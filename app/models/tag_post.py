from django.db import models

from .post import Post
from .student import Student


class TagPost(models.Model):
    admin = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="tag_posts"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="tag_posts"
    )
    name = models.CharField(max_length=255)
    background_color = models.CharField(max_length=100)
    is_selected = models.BooleanField(default=False)
