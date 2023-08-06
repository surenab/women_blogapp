from django import forms
from .models import Blog
from .models import Message

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

    title = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'Title'}))
    description = forms.CharField(label="", widget=forms.Textarea(
        attrs={'placeholder': 'Blog Description'}))
    blog_category = forms.ChoiceField(
        label="", choices=BLOG_CATEGORIES, widget=forms.Select())
    images = forms.ImageField(label="Images related to your blog")

    class Meta:
        model = Blog
        fields = ["title", "description", "blog_category", "images"]




class MessageForm(forms.ModelForm):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=150, required=True)
    message = forms.CharField(max_length=1000, required=True)

    class Meta:
        model = Message
        exclude = ()

