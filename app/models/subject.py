from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=255)
    selected = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
