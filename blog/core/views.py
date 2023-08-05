from django.shortcuts import render
from django.views.generic import CreateView
from .forms import BlogForm
from django.urls import reverse_lazy
from .models import Blog
# Create your views here.


def home(request):
    bolgs = Blog.objects.all()
    return render(request, "core/home.html", context={"blogs": bolgs})


class CreateBlog(CreateView):
    form_class = BlogForm
    success_url = reverse_lazy("home")
    template_name = "core/create_blog.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
