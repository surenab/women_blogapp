from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Email address'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name",
                  "email", "password1", "password2"]
