from django import forms
from .models import Blog


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
