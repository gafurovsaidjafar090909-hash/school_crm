from django.contrib import admin

from .models import ClassRoom


@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):

    list_display = (
        "grade",
        "parallel",
        "created_at",
    )

    list_filter = (
        "grade",
        "parallel",
    )

    search_fields = (
        "parallel",
    )