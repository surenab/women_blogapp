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
        ("7", "Science and Technology")

    )
    
    blog_category= models.CharField(choices=BLOG_CATEGORIES, default="1", max_length=1)
    title = models.CharField(max_length=50)
    created_on = models.DateField(auto_now=True)
    user =models.ForeignKey(User, on_delete= models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="media", default=None, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"