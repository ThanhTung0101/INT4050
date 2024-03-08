from django.db import models

from .forum import Forum
from .student import Student


class Post(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="posts"
    )
    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=512)
    date_post = models.DateField(auto_now_add=True)
    content = models.TextField()
