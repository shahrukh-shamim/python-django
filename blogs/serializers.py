from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['title', 'author', 'updated_at']

        def update(self, instance, validated_data):
            # Custom update logic here
            instance.title = validated_data.get('title', instance.key)
            instance.content = validated_data.get('content', instance.value)

            # Example: adding custom validation
            # if not instance.title.startswith('home_'):
            #     raise serializers.ValidationError("Key must start with 'home_'")

            instance.save()
            return instance