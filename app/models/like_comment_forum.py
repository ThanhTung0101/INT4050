from django.db import models

from app.models import Post, Student


class LikeCommentForum(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="like_comment_forums"
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="like_comment_forums"
    )
