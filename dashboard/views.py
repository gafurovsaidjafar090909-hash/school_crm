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


from django.shortcuts import render

from .utils import ask_groq


def ask_view(request):

    answer = None

    if request.method == "POST":

        question = request.POST.get("question")

        answer = ask_groq(question)

    return render(
        request,
        "ask.html",
        {
            "answer": answer
        }
    )
