from django.db import models

from .forum import Forum
from .student import Student


class CommentForum(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="comment_forums"
    )
    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, related_name="comment_forums"
    )
    text = models.TextField()
    image = models.FileField(blank=True, null=True, upload_to="avatar/")
