from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import UserProfile
from django.contrib.auth.forms import SetPasswordForm



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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()

        # Create the user profile
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        # Update user profile attributes
        user_profile.first_name = user.first_name
        user_profile.last_name = user.last_name
        user_profile.save()

        return user



class UserPasswordChangeForm(SetPasswordForm):
    """
    For changing password
    """
    def __init__(self, *args, **kwargs):
        """
        updating form
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })