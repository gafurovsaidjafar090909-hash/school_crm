from django.views import View
from django.shortcuts import render, redirect

from .models import Timetable

from teachers.models import Teacher
from subjects.models import Subject
from classes.models import ClassRoom


class TimetableListView(View):

    def get(self, request):

        timetables = Timetable.objects.all().order_by(
            "day",
            "lesson_number"
        )

        return render(
            request,
            "timetable/timetable_list.html",
            {
                "timetables": timetables
            }
        )


class TimetableCreateView(View):

    def get(self, request):

        teachers = Teacher.objects.all().order_by(
            "name",
            "surname"
        )

        subjects = Subject.objects.all().order_by(
            "name"
        )

        classes = ClassRoom.objects.all().order_by(
            "grade",
            "parallel"
        )

        return render(
            request,
            "timetable/timetable_form.html",
            {
                "teachers": teachers,
                "subjects": subjects,
                "classes": classes,
            }
        )

    def post(self, request):

        teacher_id = request.POST.get("teacher")
        subject_id = request.POST.get("subject")
        class_id = request.POST.get("class_room")
        day = request.POST.get("day")
        lesson_number = request.POST.get("lesson_number")

        Timetable.objects.create(
            teacher_id=teacher_id,
            subject_id=subject_id,
            class_room_id=class_id,
            day=day,
            lesson_number=lesson_number,
        )

        return redirect("timetable_list")


class TimetableDetailView(View):

    def get(self, request, pk):

        timetable = Timetable.objects.get(pk=pk)

        return render(
            request,
            "timetable/timetable_detail.html",
            {
                "timetable": timetable
            }
        )


class MyTimetableView(View):

    def get(self, request):

        teacher = getattr(
            request.user,
            "teacher_profile",
            None
        )

        if teacher is None:

            return render(
                request,
                "teachers/my_timetable.html",
                {
                    "teacher": None,
                    "timetables": []
                }
            )

        timetables = Timetable.objects.filter(
            teacher=teacher
        ).order_by(
            "day",
            "lesson_number"
        )

        return render(
            request,
            "teachers/my_timetable.html",
            {
                "teacher": teacher,
                "timetables": timetables
            }
        )
