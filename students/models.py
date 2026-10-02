from django.db import models
from accounts.models import User


class Student(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile",
        null=True,
        blank=True
    )

    parent = models.ForeignKey(
        "parents.Parent",
        on_delete=models.SET_NULL,
        related_name="students",
        null=True,
        blank=True
    )

    class_room = models.ForeignKey(
        "classes.ClassRoom",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"