from blogs.models import Blog
from rest_framework import serializers
from authentication.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'author', 'title', 'content']
        read_only_fields = ['author']  # Make author read-only

        def create(self, validated_data):
            validated_data['author'] = self.context['request'].user
            return super().create(validated_data)