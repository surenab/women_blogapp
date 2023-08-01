from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="Username")
    email = forms.CharField(label="Email address")
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    first_name = forms.CharField(label="First_name")
    last_name = forms.CharField(label="Last_name")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]
