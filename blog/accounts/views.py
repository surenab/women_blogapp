from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
# Create your views here.


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def finish(request):
    return render(request, "registration/finish.html")


def terms_conditions(request):
    return render(request, "registration/terms_conditions.html")
