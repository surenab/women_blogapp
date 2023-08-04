
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
        ("7", "Science and Technology")

    )

    blog_category = forms.ChoiceField(
        label="", choices=BLOG_CATEGORIES, widget=forms.Select())
    title = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Title'}))
    description = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Blog Description'}))
    images = forms.ImageField(label="", widget=forms.ClearableFileInput(
        attrs={'multiple': True, 'placeholder': 'Images related to your blog'}))
    created_on = forms.DateTimeField(auto_now=True)

    class Meta:
        model = Blog
        fields = ["blog_category", "title", "description", "images"]
