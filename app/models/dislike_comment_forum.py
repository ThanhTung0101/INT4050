from django.db import models

from .forum import Forum
from .student import Student


class DisLikeCommentForum(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="dislike_comment_forums",
    )
    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, related_name="dislike_comment_forums"
    )
