from django.contrib import admin

from .models import Timetable


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):

    list_display = (
        "day",
        "lesson_number",
        "teacher",
        "subject",
        "class_room",
        "created_at",
    )

    list_filter = (
        "day",
        "lesson_number",
        "teacher",
        "subject",
        "class_room",
    )

    search_fields = (
        "teacher__first_name",
        "teacher__last_name",
        "subject__name",
    )

    ordering = (
        "day",
        "lesson_number",
    )