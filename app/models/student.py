from django.contrib.auth.models import User
from django.db import models

from constants import ConnectType

from .hobby import Hobby
from .skill import Skill


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=30)
    college_class = models.CharField(max_length=255)
    scholl = models.CharField(max_length=255)
    avatar_image = models.FileField(upload_to="avatar/", blank=True, null=True)

    skills = models.ManyToManyField(
        Skill, blank=True, null=True, related_name="students"
    )
    hobby = models.ManyToManyField(
        Hobby, blank=True, null=True, related_name="students"
    )
    connect_type = models.CharField(
        choices=ConnectType.CHOICES, default=ConnectType.DEFAULT
    )

    fb_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"Student_id {self.student_id}"

    def full_name(self):
        return self.user.first_name + self.user.last_name
