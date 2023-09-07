from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import SignUpForm
from core.forms import UserProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from .forms import UserPasswordChangeForm
# Create your views here.


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return super().get_context_data(**kwargs)


def terms_conditions(request):
    return render(request, "registration/terms_conditions.html")




class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    Change password
    """
    form_class = UserPasswordChangeForm
    template_name = 'registration/user_password_change.html'
    success_message = 'Your password changed'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Changing Password'
        return context

    def get_success_url(self):
        return reverse_lazy('my_blogs')