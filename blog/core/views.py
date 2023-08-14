from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import BlogForm
from .models import Blog
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import BlogFilter


# Create your views here.

class Home(FilterView):

    context_object_name = "blogs"
    filterset_class = BlogFilter
    template_name = "core/home.html"

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


class CreateBlog(BlogBase, CreateView):
    template_name = "core/create_blog.html"


    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Blog was created successfully!")
        return super().form_valid(form)



class MyBlog(LoginRequiredMixin, FilterView):
    model = Blog
    context_object_name = "blogs"
    template_name = "core/blog_list.html"
    filterset_class = BlogFilter
    paginate_by = 2

    def get_queryset(self):
        queryset = super(MyBlog, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        most_viewed_blogs = Blog.objects.order_by('-view_count')[:5] 
        context['most_viewed_blogs'] = most_viewed_blogs
        return context


      
class MyBlogDetail(BlogBase, DetailView):
    template_name = "core/blog_detail.html"

    def get_queryset(self):
        queryset = super(MyBlogDetail, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset



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


class MyBlogFilter(MyBlog):

    template_name = "core/blogs_filter.html"