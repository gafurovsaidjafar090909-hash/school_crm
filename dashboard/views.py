from django.views import View
from django.shortcuts import render


class DashboardView(View):

    def get(self, request):
        role = request.user.role
        if role == "director":
            template = "dashboard/director.html"
        elif role == "teacher":
            template = "dashboard/teacher.html"
        elif role == "student":
            template = "dashboard/student.html"
        elif role == "parent":
            template = "dashboard/parent.html"
        else:
            template = "dashboard/dashboard.html"
        return render(request, template)