from django.db import models

from .post import Post
from .student import Student


class ForumCommentLike(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="forum_comment_likes"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="forum_comment_likes"
    )
