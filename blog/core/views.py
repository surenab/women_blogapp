from django.shortcuts import render
from django.views.generic import CreateView
from .forms import BlogForm
from django.urls import reverse_lazy
from .models import Blog

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
        return super().form_valid(form)


def signle_post(request):
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