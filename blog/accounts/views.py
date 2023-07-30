from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm
from django.http import HttpResponse

# Create your views here.

class Signup(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def home(request):
    return HttpResponse("home page")


def home2(request):
    return HttpResponse("home page aftre logout: NO user info")

