

from django.shortcuts import render, redirect, get_list_or_404
from django.forms.models import BaseModelForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from typing import Any, Dict
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest
from .forms import BlogForm, MessageForm, BlogCommentForm
from .models import Blog, BlogComment, AboutTeam, TeamMember
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from .filters import BlogFilter
from django.http import JsonResponse
from django.db.models import Q
from itertools import chain



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



class CreateBlogComment(CreateView):
    model = BlogComment
    form_class = BlogCommentForm
    success_text = "Done!"

    def get_success_url(self) -> str:
        return reverse_lazy("blog_details", kwargs={"pk": self.request.POST.get("blog")})

    def form_valid(self, form):
        form.instance.owner = self.request.user

        messages.success(self.request, "Blog Comment instanse is created!")
        return super().form_valid(form)

      
class Filters(FilterView):
    model = Blog
    context_object_name = "blogs"
    filterset_class = BlogFilter

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        most_viewed_blogs = Blog.objects.order_by('-view_count')[:5]
        context['most_viewed_blogs'] = most_viewed_blogs
        return context


class MyFilters(LoginRequiredMixin, Filters):

    def get_queryset(self):
        queryset = super(MyFilters, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class Home(Filters):
    template_name = "core/home.html"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(Home, self).get_queryset()
        return queryset.order_by('-created_on')

    def post(self, request, *args, **kwargs):
        messageForm = MessageForm(request.POST)
        if messageForm.is_valid():
            messageForm.save()
            messages.success(request, "Message submitted successfully!")
        return redirect("{% url 'home'%}")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BlogFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class Category(Home):
    template_name = "core/category.html"
    paginate_by = 6




class MyBlog(MyFilters):
    template_name = "core/blog_list.html"

    def get_paginate_by(self, queryset):
        blogs_per_page = self.request.GET.get('blogs_per_page')

        default_blogs_per_page = 7

        try:
            blogs_per_page = int(blogs_per_page)
        except (ValueError, TypeError):
            blogs_per_page = default_blogs_per_page

        blogs_per_page = max(1, min(blogs_per_page, 50))

        return blogs_per_page


class BlogDetail(DetailView):
    model = Blog
    template_name = "core/blog_detail.html"
    context_object_name = "blog"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        self.object.view_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data['comment_form'] = BlogCommentForm
        data['comments'] = BlogComment.objects.filter(blog=data['blog'])
        return data


class CreateBlogComment(CreateView):
    model = BlogComment
    form_class = BlogCommentForm
    success_text = "Created"

    def get_success_url(self) -> str:
        return reverse_lazy("blog_details", kwargs={"pk": self.request.POST.get("blog")})

    def form_valid(self, form):
        form.instance.owner = self.request.user

        messages.success(self.request, "Comment is created")
        return super().form_valid(form)


class MyBlogUpdate(BlogBase, UpdateView):
    success_text = "Blog is updated!"
    template_name = "core/blog_update.html"


class BlogDelete(DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = reverse_lazy('my_blogs')
    template_name = "core/blog_confirm_delete.html"

    def get_queryset(self):
        queryset = super(BlogDelete, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self, form):
        messages.success(self.request, "The blog was deleted.")
        return super().form_valid(form)


def single_post(request):
    blogs = Blog.objects.all()
    return render(request, "core/single_post.html", context={"blogs": blogs})



def about(request):
    team_members = TeamMember.objects.all()
    about_team = AboutTeam.objects.all()
    return render(request, "core/about.html", context={"team_members": team_members,
                                                       "about_team": about_team})



class Contact(Home):
    template_name = "core/contact.html"


def search_result(request):
    query = request.GET.get('search')
    blog_filter = BlogFilter(request.GET, queryset=Blog.objects.all())

    context = {
        'query': query,  
        'blog_filter': blog_filter,
    }

    if query:
        blog_filter_qs = blog_filter.qs.filter(
            Q(title__icontains=query) | Q(description__icontains=query))
        context['blog_filter'] = blog_filter_qs

    return render(request, 'core/search_result.html', context)


def search_suggestions(request):
    search_query = request.GET.get('q', '')

    blogs = Blog.objects.filter(
    Q(title__icontains=search_query) | Q(description__icontains=search_query)
)

    suggestions = [{'title': blog.title, 'description': blog.description}
                   for blog in blogs]
    
    return JsonResponse(suggestions, safe=False)
