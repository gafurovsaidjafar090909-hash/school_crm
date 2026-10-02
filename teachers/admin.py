from django.contrib import admin

from .models import Teacher
from .forms import TeacherAdminForm


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    form = TeacherAdminForm

    list_display = (
        "name",
        "surname",
        "user",
        "phone",
        "created_at",
    )

    list_filter = (
        "subjects",
    )

    search_fields = (
        "name",
        "surname",
        "phone",
        "user__username",
    )