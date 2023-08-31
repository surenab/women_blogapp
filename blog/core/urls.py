"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    CreateBlogComment,
    about

)


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("my-blogs/", MyBlog.as_view(), name="my_blogs"),
    path("blog-details/<int:pk>",
         BlogDetail.as_view(), name="blog_details"),
    path("my-blogs/update/<int:pk>", MyBlogUpdate.as_view(), name="my_blog_update"),
    path("my-blogs/delete/<int:pk>", BlogDelete.as_view(), name="my_blog_delete"),
    path("createblog/", CreateBlog.as_view(), name="createblog"),
    path("singlepost/", single_post, name="singlepost"),
    path("about/", about, name="about"),
    path("contact/", Contact.as_view(), name="contact"),
    path("searchresult/", search_result, name="searchresult"),
    path("category/", Category.as_view(), name="category"),
    path("create_comment", CreateBlogComment.as_view(), name="create_comment"),
    path("details/<int:pk>", BlogDetail.as_view(), name="blog_details"),
]
