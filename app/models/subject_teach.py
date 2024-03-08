from django.db import models

from constants import Experiment, SubjectName

from .student import Student


class SubjectTeach(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="subjects_teach"
    )
    name = models.CharField(
        choices=SubjectName.CHOICES, default=SubjectName.MATH
    )
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    description = models.TextField(blank=True)
    experiment = models.CharField(
        choices=Experiment.CHOICES, default=Experiment.PRO
    )
