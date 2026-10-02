from django.db import models


class ClassRoom(models.Model):

    grade = models.PositiveIntegerField()

    parallel = models.CharField(
        max_length=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.grade}-{self.parallel}"