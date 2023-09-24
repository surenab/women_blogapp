from django import forms
from .models import Blog, Message, BlogComment, Subscription
from .filters import BlogFilter  # Import your BlogFilter


class BlogFilterForm(forms.Form):
    SORT_CHOICES = BlogFilter.SORT_CHOICES  # Get SORT_CHOICES from your BlogFilter

    sort_by = forms.ChoiceField(
        choices=SORT_CHOICES,
        label='Sort By',
        required=False,
        widget=forms.Select(attrs={'style': 'width: 300px;'})
    )
    search = forms.CharField(
        label='Search',
        required=False,
        widget=forms.TextInput(attrs={'style': 'width: 300px;'})
    )
    blog_category = forms.ModelChoiceField(
        queryset=Blog.objects.all(),
        label='Blog Category',
        required=False,
        empty_label='All',
        widget=forms.Select(attrs={'style': 'width: 300px;'})
    )


class BlogForm(forms.ModelForm):

    BLOG_CATEGORIES = Blog.BLOG_CATEGORIES

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
        fields = ["full_name", "email", "subject", "message"]


class BlogCommentForm(forms.ModelForm):
    text = forms.CharField(label="")

    class Meta:
        model = BlogComment
        fields = ['text']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']
