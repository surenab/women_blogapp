from django.db import models
from django.contrib .auth import get_user_model


User = get_user_model()


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.CharField(
        max_length=100, default=None, blank=True, null=True)
    phone = models.CharField(
        max_length=15, default=None, blank=True, null=True)
    city = models.CharField(
        max_length=100, default=None, blank=True, null=True)

    photo = models.ImageField(
        upload_to="Media", default=None, null=True, blank=True)


    def __str__(self):
        return f"{self.user.username} {self.profession}"


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    User.profile = property(
        lambda u: UserProfile.objects.get_or_create(user=u)[0])
