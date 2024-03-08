from django.db import models

from constants import SubjectName

from .student import Student


class SubjectLearn(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="subjects_learn"
    )
    name = models.CharField(
        choices=SubjectName.CHOICES, default=SubjectName.MATH
    )
    description = models.TextField(blank=True)
    price_propose = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True
    )
