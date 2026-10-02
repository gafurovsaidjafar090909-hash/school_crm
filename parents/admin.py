from django.contrib import admin

from .models import Parent
from .forms import ParentAdminForm


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):

    form = ParentAdminForm

    list_display = (
        "first_name",
        "last_name",
        "user",
        "phone",
        "created_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "phone",
        "user__username",
    )