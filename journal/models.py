from django.db import models

from teachers.models import Teacher
from students.models import Student
from subjects.models import Subject
from classes.models import ClassRoom


class Journal(models.Model):
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    class_room = models.ForeignKey(
        ClassRoom,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    attendance = models.BooleanField(
        default=True
    )

    score = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.date}"