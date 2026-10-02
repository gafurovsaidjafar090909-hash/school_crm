from django.views import View
from django.shortcuts import render, redirect
from journal.models import Journal
from .models import Parent
from timetable.models import Timetable


class ParentListView(View):
    def get(self, request):
        parents = Parent.objects.all()
        return render(request,"parents/parent_list.html",{"parents": parents})


class ParentCreateView(View):
    def get(self, request):
        return render(request,"parents/parent_form.html")
    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        Parent.objects.create(first_name=first_name,last_name=last_name,phone=phone,address=address)
        return redirect("parent_list")


class ParentDetailView(View):
    def get(self, request, pk):
        parent = Parent.objects.get(pk=pk)
        return render(request,"parents/parent_detail.html",{"parent": parent})



class ChildrenGradesView(View):
    def get(self, request):
        parent = getattr(request.user,"parent_profile",None)
        if parent is None:
            return render(request,"parents/children_grades.html",{"parent": None,"journals": []})
        children = parent.students.all()
        journals = Journal.objects.filter(student__in=children).select_related("student","subject","teacher","class_room").order_by("-date")
        return render(request,"parents/children_grades.html",{"parent": parent,"journals": journals})


class ChildrenAttendanceView(View):
    def get(self, request):
        parent = getattr(request.user,"parent_profile",None)
        if parent is None:
            return render(request,"parents/attendance.html",{"parent": None,"journals": []})
        children = parent.students.all()
        journals = Journal.objects.filter(student__in=children).select_related("student","subject","class_room").order_by("-date")
        return render(request,"parents/attendance.html",{"parent": parent,"journals": journals})


class ChildrenTimetableView(View):
    def get(self, request):
        parent = getattr(request.user,"parent_profile",None)
        if parent is None:
            return render(request,"parents/timetable.html",{"parent": None,"timetables": []})
        children = parent.students.all()
        timetables = Timetable.objects.filter(
            class_room__in=children.values("class_room")).select_related("teacher","subject","class_room").order_by("day","lesson_number")
        return render(request,"parents/timetable.html",{"parent": parent,"timetables": timetables})


class MyChildrenView(View):
    def get(self, request):
        parent = getattr(request.user,"parent_profile",None)
        if parent is None:
            return render(request,"parents/my_children.html",{"parent": None,"students": []})
        students = parent.students.all()
        return render(request,"parents/my_children.html",{"parent": parent,"students": students})