from django.db import models


class Slider(models.Model):
    image = models.FieldFile(upload_to="slider/")
    name = models.CharField(max_length=512, blank=True)
    link = models.URLField()

    def __str__(self):
        return self.name
