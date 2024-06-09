from blogs.models import Blog
from rest_framework import serializers
from authentication.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = ['id', 'author', 'title', 'content']