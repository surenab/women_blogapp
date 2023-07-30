from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm

# Create your views here.

class Signup(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

