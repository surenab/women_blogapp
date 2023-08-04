from django.db import models
from django.contrib .auth import get_user_model

class Blog(models.Model):
  
    BLOG_TYPES = (
        ("1", "Travel"),
        ("2", "Sport") ,
        ("3", "Natural"),
        ("4", "Funny animals"),
        ("5", "nature")
    )
    
    blog_type = models.CharField(choices=BLOG_TYPES, default="1", max_length=1)
    title = models.CharField(max_length=50)
    create_date = models.DateField()
    user =models.ForeignKey(User, on_delete= models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="Media", default=None, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"
