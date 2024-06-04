from django.db import models

from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    pass

# Create your models here.
class User(models.AbstractUser):
    username=models.CharField(max_length=50, unique=True)
    email=models.CharField(max_length=500, unique=True)
    phone=models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_sales_rep = models.BooleanField(default=False)

    objects=CustomUserManager()

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return f"<User {self.email}"