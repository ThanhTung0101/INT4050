from django.db import models

from .forum import Forum
from .student import Student


class ForumComment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="forum_comments"
    )
    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, related_name="forum_comments"
    )
    text = models.TextField()
    image = models.FileField(blank=True, null=True, upload_to="avatar/")

    def __str__(self):
        return f"Comment Forum: {self.text}"
