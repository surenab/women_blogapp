from django.test import TestCase
from .models import UserProfile
from django.contrib .auth import get_user_model
from .forms import  BlogForm
from .models import Blog
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile



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





# TestCase for BlogForm form

class  BlogFormTest(TestCase):
    def setUp(self) -> None:
        self.form = BlogForm()

    def test_form_labels(self):
        self.assertTrue(self.form.fields["title"].label is None or self.form.fields["title"].label == "title")
        self.assertTrue(self.form.fields["description"].label is None or self.form.fields["description"].label == "description")
        self.assertTrue(self.form.fields["blog_category"].label is None or self.form.fields["blog_category"].label == "blog_categorye")
        self.assertTrue(self.form.fields["image"].label is None or self.form.fields["image"].label == "image")

    def tearDown(self) -> None:
        del self.form





# TestCase for Blog model

class  BlogTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="alla", email="allaasoyan@gmail.com", password="123456a"
        )
        self.first_blog =  Blog.objects.create(
            title="Test1",
            description="Desc1",
            blog_category="1",
            user=self.user,
            image= SimpleUploadedFile(name='baby.jpg', content=open('/home/almastasoyan/Desktop/Courses/women_blogapp/blog/media/Media/baby.jpg', 'rb').read())
        )



    def test_blog_str(self):
        self.assertTrue(
            f"{self.user.username}, {self.first_blog.title}, {self.first_blog.blog_category}, {self.first_blog.created_on}",
            str(self.first_blog),
        )


    def test_blog_missed_field_description(self):
        Blog.objects.create(
            title="Test1",
            blog_category="1",
            user=self.user,
            image=SimpleUploadedFile(name='baby.jpg', content=open('/home/almastasoyan/Desktop/Courses/women_blogapp/blog/media/Media/baby.jpg', 'rb').read())
        )
        
        

    def tearDown(self) -> None:
        del self.user
        del self.first_blog

        
