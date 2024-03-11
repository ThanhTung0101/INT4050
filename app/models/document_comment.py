from django.db import models

from .document import Document
from .student import Student


class DocumentComment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="document_comments"
    )
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="document_comments"
    )
    text = models.TextField()

    def __str__(self):
        return f"Comment Document: {self.text}"
