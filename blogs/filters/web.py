# filters.py
import django_filters
from blogs.models import Blog

class BlogFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__id', lookup_expr='icontains')
    status = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Blog
        fields = ['title', 'author', 'created_at']
