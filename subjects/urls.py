from django.urls import path

from .views import *


urlpatterns = [

    path("",SubjectListView.as_view(),name="subject_list"),
    path("create/",SubjectCreateView.as_view(),name="subject_create"),
    path("<int:pk>/",SubjectDetailView.as_view(),name="subject_detail"),

]