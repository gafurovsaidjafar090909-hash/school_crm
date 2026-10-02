from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path("admin/", admin.site.urls),

    path("accounts/", include("accounts.urls")),

    path("dashboard/", include("dashboard.urls")),

    path("teachers/", include("teachers.urls")),

    path("students/", include("students.urls")),

    path("parents/", include("parents.urls")),

    path("subjects/", include("subjects.urls")),

    path("classes/", include("classes.urls")),

    path("timetable/", include("timetable.urls")),

    path("journal/", include("journal.urls")),

   path(
        "classes/",
        include("classes.urls")
    ),
    path("journal/", include("journal.urls")),
]

