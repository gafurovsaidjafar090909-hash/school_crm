from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("School information", {
            "fields": ("role",)
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("School information", {
            "fields": ("role",)
        }),
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "role",
        "is_staff",
        "is_active",
    )

    list_filter = (
        "role",
        "is_staff",
        "is_active",
    )

    search_fields = (
        "username",
        "first_name",
        "last_name",
    )