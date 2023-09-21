from django.urls import path
from accounts.views import edit_profile
from .views import (

    Category,
    Home,
    CreateBlog,
    MyBlog,
    BlogDelete,
    MyBlogUpdate,
    BlogDetail,
    Contact,
    search_result,
    search_suggestions,
    CreateBlogComment,
    About,
    subscribe,
    thank_you,
)

from . import views


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("my-blogs/", MyBlog.as_view(), name="my_blogs"),
    path("my-blogs/update/<int:pk>", MyBlogUpdate.as_view(), name="my_blog_update"),
    path("my-blogs/delete/<int:pk>", BlogDelete.as_view(), name="my_blog_delete"),
    path("createblog/", CreateBlog.as_view(), name="create_blog"),
    path("about/", About.as_view(), name="about"),
    path("contact/", Contact.as_view(), name="contact"),
    path('search/', search_result, name='search_result'),
    path("category/", Category.as_view(), name="category"),
    path('search-suggestions/', search_suggestions, name='search_suggestions'),
    path("create_comment", CreateBlogComment.as_view(), name="create_comment"),
    path("details/<int:pk>", BlogDetail.as_view(), name="blog_detail"),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('subscribe/', subscribe, name='subscribe'),
    path('thank_you/', thank_you, name='thank_you'),

]
