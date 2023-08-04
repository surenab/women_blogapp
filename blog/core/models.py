from django.db import models
from django.contrib .auth import get_user_model

class Blog(models.Model):
    # User= get_user_model

    Blog_types= (
       ( "1", "Travel"),
       ("2", "Sport") ,
        ("3", "Natural"),
        ("4", "Funny animals"),
        ("5", "nature"),
    )
    Blog_type = models.CharField(choices=Blog_types, default="1", max_length=1)
    title= models.CharField(max_length=50)
    
    create_data= models.DateField()
    # username=models.ForeignKey(User, on_delete= models.CASCADE)
    description= models.TextField()
    image= models.ImageField( upload_to="Media", default=None, null=True, blank=True)
