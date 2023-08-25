
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from typing import Any
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest
from .forms import BlogForm, MessageForm
from .models import Blog
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import BlogFilter


# Create your views here.


class Base(LoginRequiredMixin, CreateView):
    def get_queryset(self):
        queryset = super(Base, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class BlogBase(Base):
    model = Blog
    form_class = BlogForm
    context_object_name = "blog"
    success_url = reverse_lazy("my_blogs")
    success_text = ""

    def form_valid(self, form):
        messages.success(self.request, self.success_text)
        return super().form_valid(form)


class CreateBlog(BlogBase):
    template_name = "core/create_blog.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Blog was created successfully!")
        return super().form_valid(form)


class MyFilters(LoginRequiredMixin, FilterView):
    model = Blog
    context_object_name = "blogs"
    filterset_class = BlogFilter

    def get_queryset(self):
        queryset = super(MyFilters, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        most_viewed_blogs = Blog.objects.order_by('-view_count')[:3]
        context['most_viewed_blogs'] = most_viewed_blogs
        return context


class Home(MyFilters):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        messageForm = MessageForm(request.POST)
        if messageForm.is_valid():
            messageForm.save()
            messages.success(request, "Message submitted successfully!")

        return redirect("{% url 'home'%}")


class MyBlog(MyFilters):
    template_name = "core/blog_list.html"
    paginate_by = 2


class MyBlogDetail(BlogBase, DetailView):
    template_name = "core/blog_detail.html"

    def get_queryset(self):
        queryset = super(MyBlogDetail, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.view_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class MyBlogUpdate(BlogBase, UpdateView):
    success_text = "Blog is updated!"
    template_name = "core/blog_update.html"


# This view dosn't delete the blog

# class MyBlogDelete(BlogBase, DeleteView):
#   success_text = "Blog is deleted!"
#   template_name = "core/blog_confirm_delete.html"

class MyBlogDelete(DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = reverse_lazy('my_blogs')
    template_name = "core/blog_confirm_delete.html"

    def get_queryset(self):
        queryset = super(MyBlogDelete, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        messages.success(self.request, "The blog was deleted.")
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
