from django.db import models
from django.contrib .auth import get_user_model

User = get_user_model()


class Blog(models.Model):

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

    blog_category = models.CharField(
        choices=BLOG_CATEGORIES, default="1", max_length=2)
    title = models.CharField(max_length=150)
    created_on = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(
        upload_to="Media", default=None, null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0) 

    def __str__(self) -> str:
        return f"{self.user.username} , {self.title}, {self.blog_category}, {self.created_on}"

class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now=True)