from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticatedOrReadOnly
from api.serializers.blogs import serializers
from rest_framework.decorators import permission_classes
from blogs.models import Blog
from rest_framework.permissions import IsAuthenticated
from blogs.services import BlogService
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from blogs.filters.api import BlogFilter

# Create your views here.
class BlogListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.BlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BlogFilter
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissions]

    def get_queryset(self):
        return BlogService.get_all_blogs()
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(data={"error": "Authentication required"}, status=status.HTTP_403_FORBIDDEN)
        
        return super().post(request, *args, **kwargs)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogService.get_all_blogs()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissions]
    
    def get_object(self):
        obj = super().get_object()
        # Additional custom permissions or logic can be added here
        return obj

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.author and not request.user.is_superuser:
            return Response(data={"error": "You are not allowed to update this blog post"}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user != instance.author and not request.user.is_superuser:
            return Response(data={"error": "You are not allowed to delete this blog post"}, status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)