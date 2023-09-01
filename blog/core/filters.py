from django_filters import FilterSet, CharFilter, ChoiceFilter
from django.db.models import Q, F
from .models import Blog


class BlogFilter(FilterSet):
    SORT_CHOICES = (
        ('newest', 'Newest Blogs'),
        ('oldest', 'Oldest Blogs'),
        ('most_viewed', 'Most Viewed Blogs')
    )

    sort_by = ChoiceFilter(choices=SORT_CHOICES,
                           method='custom_sort', label='Sort By')
    search = CharFilter(method='custom_search', label='Search')

    class Meta:
        model = Blog
        fields = {
            'blog_category': ['exact'],
        }

    def custom_search(self, queryset, name, value):
        return queryset.filter(
        Q(title__icontains=value) | Q(description__icontains=value)
    )


    def custom_sort(self, queryset, name, value):
        if value == 'newest':
            return queryset.order_by('-created_on')
        elif value == 'oldest':
            return queryset.order_by('created_on')
        elif value == 'most_viewed':
            return queryset.annotate(blog_view_count=F('view_count')).order_by('-blog_view_count')
        return queryset
