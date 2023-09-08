from django.test import TestCase
from .models import UserProfile
from django.contrib .auth import get_user_model

# Create your tests here.
User = get_user_model()


# TestCase for UserProfile model
class UserProfileTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.first_userprofile = UserProfile.objects.create(
            profession="singer",
            phone="+37493495544",
            city="Yerevan",
            photo="aaa.jpg",
            user=self.user
        )

        self.second_userprofile = UserProfile.objects.create(
            profession="singer",
            photo="aaa.jpg",
            user=self.user
        )
        self.third_userprofile = UserProfile.objects.create(
      
            user=self.user
        )
    def test_userprofile_str(self):
        self.assertEqual(f"{self.first_userprofile.user.username} {self.first_userprofile.profession}", str(self.first_userprofile))

    def test_userprofile_city(self):
        self.assertEqual(self.second_userprofile.city, None)

    def tearDown(self) -> None:
        del self.user
        del self.first_userprofile
