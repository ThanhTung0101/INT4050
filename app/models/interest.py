from django.db import models


class Interest:
    name = models.CharField(max_length=50)
    percent = models.PositiveIntegerField(default=0)
