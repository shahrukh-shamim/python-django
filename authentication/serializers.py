from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSignUpSerializer(serializers.ModelSerializer):
    
    username=serializers.CharField(max_length=25)
    email=serializers.EmailField(max_length=80)
    age = serializers.IntegerField(required=False)
    password=serializers.CharField(
        min_length=8,
        write_only=True,
        required=True,
        # help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model=User
        fields=['username', 'email', 'password', 'age']

    def validate(self, attrs):
        username_exists=User.objects.filter(username=attrs['username']).exists()
        email_exists=User.objects.filter(email=attrs['email']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="Username is requried")
        
        if email_exists:
            raise serializers.ValidationError(detail="Email is not provided")
        
        return super().validate(attrs)
    
    def create(self,validated_data):
        new_user=User(**validated_data)

        new_user.password=make_password(validated_data.get('password'))

        new_user.save()

        return new_user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'age', 'first_name', 'last_name']
        read_only_fields = fields

    def create(self, validated_data):
        raise serializers.ValidationError("This serializer is read-only and cannot create records.")

    def update(self, instance, validated_data):
        raise serializers.ValidationError("This serializer is read-only and cannot update records.")