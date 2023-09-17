from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm, UserProfileForm, UserPasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth import login

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required

from .models import UserProfile

from core.models import Blog


# Create your views here.


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(
            self.request, "The account was created.")
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


class UserAccount(TemplateView):
    template_name = "registration/user_account.html"
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            user_profile = get_object_or_404(
                UserProfile, user=self.request.user)
            context['user_profile'] = user_profile

        context['user_blogs'] = Blog.objects.filter(
            user=self.request.user).order_by('-created_on')

        return context

    def get_paginate_by(self, queryset):
        blogs_per_page = self.request.GET.get('blogs_per_page')

        default_blogs_per_page = 3

        try:
            blogs_per_page = int(blogs_per_page)
        except (ValueError, TypeError):
            blogs_per_page = default_blogs_per_page

        blogs_per_page = max(1, min(blogs_per_page, 50))

        return blogs_per_page

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            user_profile = self.request.user.profile
            form = UserProfileForm(
                request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('user_account')
            return render(request, 'registration/user_account.html', {'form': form})
        else:
            return redirect('login')


@login_required
def edit_profile(request):

    user_profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            if not request.FILES.get('photo'):
                form.cleaned_data.pop('photo')
            form.save()
            return redirect('user_account')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'registration/edit_profile.html', {'form': form})
