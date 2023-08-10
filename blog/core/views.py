from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import BlogForm
from django.urls import reverse_lazy
from .forms import BlogForm
from .models import Blog
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    return render(request, "core/home.html", context={"blogs": blogs})


class CreateBlog(CreateView):
    form_class = BlogForm
    success_url = reverse_lazy("home")
    template_name = "core/create_blog.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Blog was created successfully!")
        return super().form_valid(form)


class MyBlog(LoginRequiredMixin, ListView):
    model = Blog

    context_object_name = "blogs"
    template_name = "core/blog_list.html"

    def get_queryset(self):
        queryset = super(MyBlog, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class MyBlogDetail(LoginRequiredMixin, DetailView):
    model = Blog
    context_object_name = "blog"

    def get_queryset(self):
        queryset = super(MyBlogDetail, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class MyBlogUpdate(LoginRequiredMixin, UpdateView):
    model = Blog
    context_object_name = "blog"
    form_class = BlogForm
    success_url = reverse_lazy("my_todos")

    def get_queryset(self):
        queryset = super(MyBlogUpdate, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        messages.success(self.request, "Blog instance is updated!")
        return super().form_valid(form)


class MyBlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    context_object_name = "blog"
    success_url = reverse_lazy("my_blogs")

    def get_queryset(self):
        queryset = super(MyBlogDelete, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        messages.info(self.request, "Blog instance is deleted!")
        return super().form_valid(form)


def single_post(request):
    blogs = Blog.objects.all()
    return render(request, "core/single_post.html", context={"blogs": blogs})


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")


def category(request):
    blogs = Blog.objects.all()
    return render(request, "core/category.html", context={"blogs": blogs})


def search_result(request):
    blogs = Blog.objects.all()
    return render(request, "core/search_result.html", context={"blogs": blogs})
