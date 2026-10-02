from django.views import View
from django.shortcuts import render, redirect

from .models import ClassRoom


class ClassListView(View):
    def get(self, request):
        classes = ClassRoom.objects.all()
        return render(request,"classes/class_list.html",{"classes": classes})


class ClassCreateView(View):
    def get(self, request):
        return render(request,"classes/class_form.html")
    def post(self, request):
        grade = request.POST.get("grade")
        parallel = request.POST.get("parallel")
        ClassRoom.objects.create(grade=grade,parallel=parallel)
        return redirect("class_list")


class ClassDetailView(View):
    def get(self, request, pk):
        class_room = ClassRoom.objects.get(pk=pk)
        return render(request,"classes/class_detail.html",{"class_room": class_room})