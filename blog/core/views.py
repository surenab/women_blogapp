from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CreateBlogForm
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    return render(request, "core/home.html")


class CreateBlog(CreateView):
    form_class = CreateBlogForm
    success_url = reverse_lazy("home")
    template_name = "core/create_blog.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
