from django.db import models

from .forum import Forum
from .student import Student


class ForumCommentDislike(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="forum_comment_dislikes",
    )
    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, related_name="forum_comment_dislikes"
    )
