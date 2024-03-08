from django.db import models

from .student import Student


class Category(models.Model):
    admin = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="categories"
    )
    name = models.CharField(max_length=255)
    background_color = models.CharField(max_length=100)
    is_selected = models.BooleanField(default=False)
