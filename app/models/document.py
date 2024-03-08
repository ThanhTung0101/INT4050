from django.db import models

from constants import SubjectName

from .student import Student


class Document(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="documents"
    )
    title = models.CharField(max_length=512)
    document_file = models.FileField(upload_to="document/")
    description = models.TextField(blank=True)
    subject = models.TextField(
        choices=SubjectName, default=SubjectName.ENGLISH
    )
