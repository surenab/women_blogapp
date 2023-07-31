from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import format_html


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-input'}))
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))


    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class LogInForm(UserCreationForm):
    username = forms.CharField(
        label="Username", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ["username", "password"]