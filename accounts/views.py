from django.views import View
from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request,"accounts/register.html",{"form": form})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
        return render(request,"accounts/register.html",{"form": form})


    
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request,"accounts/login.html",{"form": form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request, user)
            return redirect("dashboard")
        return render(request,"accounts/login.html",{"form": form})