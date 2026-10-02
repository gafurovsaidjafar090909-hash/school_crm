from django.urls import path

from .views import *



app_name = "teachers"


urlpatterns = [
path("", TeacherListView.as_view(), name="teacher_list"),
    path("create/",TeacherCreateView.as_view(),name="teacher_create"),
    path("my-subjects/",MySubjectsView.as_view(),name="my_subjects"),
    path("my-timetable/",MyTimetableView.as_view(),name="my_timetable"),
    path("<int:pk>/",TeacherDetailView.as_view(),name="teacher_detail"),

]
