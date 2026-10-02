from django.urls import path
from .views import *


urlpatterns = [
    path("",DashboardView.as_view(),name="dashboard"),
    path("ask/", ask_view, name="ask_groq"),
]