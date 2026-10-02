from django.urls import path

from .views import (
    TimetableListView,
    TimetableCreateView,
    TimetableDetailView,
)


urlpatterns = [

    path(
        "",
        TimetableListView.as_view(),
        name="timetable_list"
    ),

    path(
        "create/",
        TimetableCreateView.as_view(),
        name="timetable_create"
    ),

    path(
        "<int:pk>/",
        TimetableDetailView.as_view(),
        name="timetable_detail"
    ),

]