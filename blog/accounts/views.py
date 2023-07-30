from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm, LogInForm
from django.urls import reverse_lazy
# Create your views here.


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LogIn(CreateView):
    form_class = LogInForm
    success_url = reverse_lazy("home")
    template_name = "registration/login.html"


def logout1(request):
    return render(request, "registration/logout.html")


def finish(request):
    return render(request, "registration/finish.html")


def home(request):
    return render(request, "registration/home.html")
