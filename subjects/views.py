from django.views import View
from django.shortcuts import render, redirect

from .models import Subject
from .forms import SubjectForm


class SubjectListView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        return render(request,"subjects/subject_list.html",{"subjects": subjects})

class SubjectCreateView(View):
    def get(self, request):
        form = SubjectForm()
        return render(request,"subjects/subject_form.html",{"form": form})
    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subject_list")
        return render(request,"subjects/subject_form.html",{"form": form})


class SubjectDetailView(View):
    def get(self, request, pk):
        subject = Subject.objects.get(pk=pk)
        return render(request,"subjects/subject_detail.html",{"subject": subject})