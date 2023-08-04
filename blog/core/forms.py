from django import forms
from .models import Blog



class BlogForm(forms.ModelForm):

    BLOG_TYPES = (
        ("1", "Travel"),
        ("2", "Sport") ,
        ("3", "Nature"),
        ("4", "Animals"),
        ("5", "Food"),
        ("6", "DIY and Crafts"),
        ("7", "Science and Technology")

    )

    blog_type = forms.ChoiceField(choices=BLOG_TYPES)
    created_on = forms.DateField(widget=forms.DateTimeField())

    class Meta:
        model = Blog
        fields = ["blog_type", "title", "created_on", "description", "image"]
