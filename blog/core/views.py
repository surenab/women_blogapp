from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import BlogForm, MessageForm
from .models import Blog

# Create your views here.


def home(request) -> HttpResponse:

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    blogs = Blog.objects.all()
    return render(request, "core/home.html", context={"blogs": blogs})


class CreateBlog(CreateView):
    form_class = BlogForm
    success_url = reverse_lazy("home")
    template_name = "core/create_blog.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
