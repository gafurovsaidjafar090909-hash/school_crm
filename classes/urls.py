from django.urls import path
from .views import *
from django.urls import path



urlpatterns = [
    path("",ClassListView.as_view(),name="class_list"),
    path("create/",ClassCreateView.as_view(),name="class_create"),
    path("<int:pk>/",ClassDetailView.as_view(),name="class_detail"),
    path("",ClassListView.as_view(),name="class_list"),
    path("<int:pk>/",ClassDetailView.as_view(),name="class_detail"),
    
]