from django.contrib import admin

from .models import Journal


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "teacher",
        "subject",
        "class_room",
        "date",
        "attendance",
        "score",
    )

    list_filter = (
        "teacher",
        "subject",
        "class_room",
        "attendance",
        "date",
    )

    search_fields = (
        "student__user__username",
        "student__first_name",
        "student__last_name",
    )