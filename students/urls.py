from django.urls import path

from .views import *

urlpatterns = [

path("",StudentListView.as_view(),name="student_list"),
path("create/",StudentCreateView.as_view(),name="student_create"),
path("<int:pk>/",StudentDetailView.as_view(),name="student_detail"),
path("my-profile/",MyProfileView.as_view(),name="my_profile"),
path("my-timetable/",MyTimetableView.as_view(),name="student_my_timetable"),
path("my-grades/",MyGradesView.as_view(),name="student_my_grades"),
path("my-attendance/",MyAttendanceView.as_view(),name="student_my_attendance"),
]