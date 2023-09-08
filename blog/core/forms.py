from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Blog, Message, BlogComment, UserProfile
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):

    BLOG_CATEGORIES = (
        ("1", "Travel"),
        ("2", "Sport"),
        ("3", "Nature"),
        ("4", "Animals"),
        ("5", "Food"),
        ("6", "DIY and Crafts"),
        ("7", "Science and Technology"),
        ("8", "Fashion"),
        ("9", "Medicine"),
        ("10", "Psycology"),
        ("11", "Art"),
    )

    title = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Title'}))
    description = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Blog Description'}))
    blog_category = forms.ChoiceField(
        label="", choices=BLOG_CATEGORIES, widget=forms.Select())
    image = forms.ImageField(label="")

    class Meta:
        model = Blog
        fields = ["title", "description", "blog_category", "image"]


class MessageForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=150, required=True)
    message = forms.CharField(max_length=1000, required=True)

    class Meta:
        model = Message
        exclude = ()


class BlogCommentForm(forms.ModelForm):
    text = forms.Textarea()

    class Meta:
        model = BlogComment
        fields = ['text']


class UserProfileForm(forms.ModelForm):
    # Add fields for first_name and last_name
    first_name = forms.CharField(
        max_length=30, required=True, label="First Name")
    last_name = forms.CharField(
        max_length=30, required=True, label="Last Name")

    photo = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'clearablefileinput'}), label='')

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'profession',
                  'city', 'phone']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Include first_name and last_name fields from the User model
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name

    def save(self, commit=True):
        # Save the first_name and last_name fields back to the User model
        self.instance.user.first_name = self.cleaned_data['first_name']
        self.instance.user.last_name = self.cleaned_data['last_name']

        # Save the UserProfile instance
        user_profile = super(UserProfileForm, self).save(commit=commit)

        if commit:
            # Save the User model
            self.instance.user.save()

        return user_profile
