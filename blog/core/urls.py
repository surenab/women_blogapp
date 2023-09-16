
from django.urls import path
from .views import (

    Category,
    Home,
    CreateBlog,
    MyBlog,
    BlogDelete,
    MyBlogUpdate,
    BlogDetail,
    single_post,
    Contact,
    search_result,
    search_suggestions,
    CreateBlogComment,
    subscribe,
    thank_you
    About,
)

from accounts.views import (UserAccount, edit_profile)


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("my-blogs/", MyBlog.as_view(), name="my_blogs"),
    path("my-blogs/update/<int:pk>", MyBlogUpdate.as_view(), name="my_blog_update"),
    path("my-blogs/delete/<int:pk>", BlogDelete.as_view(), name="my_blog_delete"),
    path("user_account/", UserAccount.as_view(), name="user_account"),
    path("createblog/", CreateBlog.as_view(), name="createblog"),
    path("singlepost/", single_post, name="singlepost"),
    path("about/", About.as_view(), name="about"),
    path("contact/", Contact.as_view(), name="contact"),
    path('search/', search_result, name='search_result'),
    path("category/", Category.as_view(), name="category"),
    path('search-suggestions/', search_suggestions, name='search_suggestions'),
    path("create_comment", CreateBlogComment.as_view(), name="create_comment"),
    path("details/<int:pk>", BlogDetail.as_view(), name="blog_details"),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('subscribe/', subscribe, name='subscribe'),
    path('thank_you/', thank_you, name='thank_you'),

]
