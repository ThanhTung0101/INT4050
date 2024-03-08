from django.db import models

from .student import Student


class MessageTwoPeople(models.Model):
    student1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="messages_two_people"
    )
    student1 = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="messages_two_people"
    )
    message = models.TextField()
