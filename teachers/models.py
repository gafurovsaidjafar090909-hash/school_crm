from django.db import models
from accounts.models import User
from subjects.models import Subject


class Teacher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="teacher_profile",
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)

    subjects = models.ManyToManyField(
        Subject,
        blank=True,
        related_name="teachers"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"