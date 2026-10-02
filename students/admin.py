from django.contrib import admin

from .models import Student
from .forms import StudentAdminForm


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    form = StudentAdminForm

    list_display = (
        "first_name",
        "last_name",
        "user",
        "parent",
        "class_room",
        "phone",
        "created_at",
    )

    list_filter = (
        "class_room",
        "parent",
    )

    search_fields = (
        "first_name",
        "last_name",
        "phone",
        "user__username",
    )