from django.db import models

from .document import Document
from .student import Student


class DocumentLike(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="document_likes"
    )
    document = models.ForeignKey(
        Document, on_delete=models.CASCADE, related_name="document_likes"
    )
