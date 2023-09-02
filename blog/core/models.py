from django.db import models
from django.contrib .auth import get_user_model
from PIL import Image


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
    created_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(
        upload_to="Media", default=None, null=True, blank=True)
    image1 = models.ImageField(
        upload_to="Media", default=None, null=True, blank=True)
    image2 = models.ImageField(
        upload_to="Media", default=None, null=True, blank=True)

    view_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user.username} , {self.title}, {self.blog_category}, {self.created_on}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 700:
            output_size = (500, 700)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)


class TeamMember(models.Model):
    full_name = models.CharField(max_length=50)
    job_position = models.CharField(max_length=50)
    about_member = models.TextField(max_length=1000)
    member_image = models.ImageField(
        upload_to="Media", default=None, null=True, blank=True)


class AboutTeam(models.Model):
    our_team = models.TextField(max_length=1000)
    team_image = models.ImageField(
        upload_to="Media", default=None, null=True, blank=True)


class BlogComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.owner.username} is commented {self.text}"
