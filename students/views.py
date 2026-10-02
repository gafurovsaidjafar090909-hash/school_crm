from django.views import View

from django.shortcuts import render, redirect

from timetable.models import Timetable

from .models import Student

from parents.models import Parent

from classes.models import ClassRoom

from journal.models import Journal


class StudentListView(View):

    def get(self, request):

        students = Student.objects.select_related(
            "parent",
            "class_room"
        ).all()

        return render(
            request,
            "students/student_list.html",
            {
                "students": students
            }
        )


class StudentCreateView(View):

    def get(self, request):

        parents = Parent.objects.all()

        classes = ClassRoom.objects.all()

        return render(
            request,
            "students/student_form.html",
            {
                "parents": parents,
                "classes": classes
            }
        )

    def post(self, request):

        first_name = request.POST.get("first_name")

        last_name = request.POST.get("last_name")

        date_of_birth = request.POST.get("date_of_birth")

        phone = request.POST.get("phone")

        address = request.POST.get("address")

        parent_id = request.POST.get("parent")

        class_id = request.POST.get("class_room")

        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth or None,
            phone=phone,
            address=address,
            parent_id=parent_id or None,
            class_room_id=class_id or None
        )

        return redirect("student_list")


class StudentDetailView(View):

    def get(self, request, pk):

        student = Student.objects.select_related(
            "parent",
            "class_room"
        ).get(pk=pk)

        return render(
            request,
            "students/student_detail.html",
            {
                "student": student
            }
        )


class MyProfileView(View):

    def get(self, request):

        student = getattr(
            request.user,
            "student_profile",
            None
        )

        return render(
            request,
            "students/my_profile.html",
            {
                "student": student
            }
        )


class MyTimetableView(View):

    def get(self, request):

        student = getattr(
            request.user,
            "student_profile",
            None
        )

        if student is None:

            return render(
                request,
                "students/my_timetable.html",
                {
                    "student": None,
                    "timetables": []
                }
            )

        if student.class_room is None:

            return render(
                request,
                "students/my_timetable.html",
                {
                    "student": student,
                    "timetables": []
                }
            )

        timetables = Timetable.objects.filter(
            class_room=student.class_room
        ).select_related(
            "teacher",
            "subject",
            "class_room"
        ).order_by(
            "day",
            "lesson_number"
        )

        return render(
            request,
            "students/my_timetable.html",
            {
                "student": student,
                "timetables": timetables
            }
        )


class MyGradesView(View):

    def get(self, request):

        student = getattr(
            request.user,
            "student_profile",
            None
        )

        if student is None:

            return render(
                request,
                "students/my_grades.html",
                {
                    "student": None,
                    "journals": []
                }
            )

        journals = Journal.objects.filter(
            student=student
        ).select_related(
            "subject",
            "class_room",
            "teacher"
        ).order_by(
            "-date"
        )

        return render(
            request,
            "students/my_grades.html",
            {
                "student": student,
                "journals": journals
            }
        )


class MyAttendanceView(View):

    def get(self, request):

        student = getattr(
            request.user,
            "student_profile",
            None
        )

        if student is None:

            return render(
                request,
                "students/my_attendance.html",
                {
                    "student": None,
                    "journals": []
                }
            )

        journals = Journal.objects.filter(
            student=student
        ).select_related(
            "subject",
            "teacher",
            "class_room"
        ).order_by(
            "-date"
        )

        return render(
            request,
            "students/my_attendance.html",
            {
                "student": student,
                "journals": journals
            }
        )