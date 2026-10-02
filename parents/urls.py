from django.urls import path

from .views import *

urlpatterns = [
    path("", ParentListView.as_view(), name="parent_list"),
    path("create/", ParentCreateView.as_view(), name="parent_create"),
    path("my-children/",MyChildrenView.as_view(),name="my_children"),
    path("children-grades/",ChildrenGradesView.as_view(),name="children_grades"),
    path("attendance/",ChildrenAttendanceView.as_view(),name="children_attendance"),
    path("timetable/",ChildrenTimetableView.as_view(),name="children_timetable"),
    path("<int:pk>/",ParentDetailView.as_view(),name="parent_detail"),
]