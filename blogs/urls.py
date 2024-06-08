from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('<str:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<str:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<str:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]