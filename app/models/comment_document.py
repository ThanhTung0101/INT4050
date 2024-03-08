from django.db import models

from .document import Document
from .student import Student


class CommentDocument(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="comment_documents"
    )
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="comment_documents"
    )
    text = models.TextField()
