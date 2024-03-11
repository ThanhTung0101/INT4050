from django.db import models


class Hobby(models.Model):
    name = models.CharField(max_length=50)
    percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
