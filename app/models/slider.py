from django.db import models


class Slider(models.Model):
    image = models.FieldFile(upload_to="slider/")
    name = models.CharField(max_length=512)
    link = models.URLField()
