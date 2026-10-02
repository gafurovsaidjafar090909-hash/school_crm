from django.views import View
from django.shortcuts import render, redirect

from .models import Teacher
from timetable.models import Timetable
from subjects.models import Subject


class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        return render(request,"teachers/teacher_list.html",{"teachers": teachers})


class TeacherCreateView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        return render(request,"teachers/teacher_form.html",{"subjects": subjects})
    def post(self, request):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        phone = request.POST.get("phone") or ""
        teacher = Teacher.objects.create(name=name,surname=surname,phone=phone)
        subject_ids = request.POST.getlist("subjects")
        if subject_ids:
            teacher.subjects.set(subject_ids)
        return redirect("teachers:teacher_list")


class TeacherDetailView(View):
    def get(self, request, pk):
        teacher = Teacher.objects.get(pk=pk)
        return render(request,"teachers/teacher_detail.html",{"teacher": teacher})


class MySubjectsView(View):
    def get(self, request):
        teacher = getattr(request.user,"teacher_profile",None)
        if teacher is None:
            return render(request,"teachers/my_subjects.html",{"teacher": None,"subjects": []})
        subjects = teacher.subjects.all()
        return render(request,"teachers/my_subjects.html",{"teacher": teacher,"subjects": subjects})


class MyTimetableView(View):
    def get(self, request):
        teacher = getattr(request.user,"teacher_profile",None)
        if teacher is None:
            return render(request,"teachers/my_timetable.html",{"teacher": None,"timetables": []})
        timetables = Timetable.objects.filter(teacher=teacher).order_by("day","lesson_number")
        return render(request,"teachers/my_timetable.html",{"teacher": teacher,"timetables": timetables})


