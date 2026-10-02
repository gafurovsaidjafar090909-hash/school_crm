from django.urls import path

from .views import (
    JournalListView,
    JournalDetailView,
    JournalCreateView,
    MyJournalView,
    ClassJournalView,
)


urlpatterns = [

    path(
        "",
        JournalListView.as_view(),
        name="journal_list"
    ),

    path(
        "create/",
        JournalCreateView.as_view(),
        name="journal_create"
    ),

    path(
        "my/",
        MyJournalView.as_view(),
        name="my_journal"
    ),

    path(
        "class/<int:pk>/",
        ClassJournalView.as_view(),
        name="journal_class"
    ),

    path(
        "<int:pk>/",
        JournalDetailView.as_view(),
        name="journal_detail"
    ),
]