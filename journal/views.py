from django.views import View
from django.shortcuts import render, redirect

from .models import Journal

from teachers.models import Teacher
from students.models import Student
from subjects.models import Subject
from classes.models import ClassRoom


class JournalListView(View):

    def get(self, request):

        journals = Journal.objects.select_related(
            "teacher",
            "student",
            "subject",
            "class_room"
        ).order_by("-date")

        return render(
            request,
            "journal/journal_list.html",
            {
                "journals": journals
            }
        )


class JournalDetailView(View):

    def get(self, request, pk):

        journal = Journal.objects.select_related(
            "student",
            "teacher",
            "subject",
            "class_room"
        ).get(pk=pk)

        return render(
            request,
            "journal/journal_detail.html",
            {
                "journal": journal
            }
        )


class JournalCreateView(View):

    def get(self, request):

        teachers = Teacher.objects.all()
        students = Student.objects.all()
        subjects = Subject.objects.all()
        classes = ClassRoom.objects.all()

        return render(
            request,
            "journal/journal_form.html",
            {
                "teachers": teachers,
                "students": students,
                "subjects": subjects,
                "classes": classes,
            }
        )

    def post(self, request):

        teacher_id = request.POST.get("teacher")
        student_id = request.POST.get("student")
        subject_id = request.POST.get("subject")
        class_id = request.POST.get("class_room")

        date = request.POST.get("date")
        score = request.POST.get("score")
        attendance = request.POST.get("attendance")

        Journal.objects.create(
            teacher_id=teacher_id,
            student_id=student_id,
            subject_id=subject_id,
            class_room_id=class_id,
            date=date,
            score=score or None,
            attendance=attendance == "present"
        )

        return redirect("journal_list")


class MyJournalView(View):

    def get(self, request):

        teacher = getattr(
            request.user,
            "teacher_profile",
            None
        )

        if teacher is None:

            return render(
                request,
                "journal/my_journal.html",
                {
                    "teacher": None,
                    "journals": []
                }
            )

        journals = Journal.objects.filter(
            teacher=teacher
        ).select_related(
            "student",
            "subject",
            "class_room"
        ).order_by("-date", "student")

        return render(
            request,
            "journal/my_journal.html",
            {
                "teacher": teacher,
                "journals": journals
            }
        )


class ClassJournalView(View):

    def get(self, request, pk):

        class_room = ClassRoom.objects.get(pk=pk)

        students = class_room.students.all()

        journals = Journal.objects.filter(
            class_room=class_room
        ).select_related(
            "teacher",
            "student",
            "subject",
            "class_room"
        ).order_by(
            "-date",
            "student"
        )

        return render(
            request,
            "journal/class_journal.html",
            {
                "class_room": class_room,
                "students": students,
                "journals": journals,
            }
        )