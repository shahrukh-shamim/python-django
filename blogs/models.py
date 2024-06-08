from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.
class Blog(models.Model):

    PUBLISHED=0
    IN_REVIEW=1
    DRAFTED=2
    BANNED=3

    BLOG_STATUSES = (
        ("PUBLISHED", "published"),
        ("IN_REVIEW", "in_review"),
        ("DRAFTED", "drafted"),
        ("BANNED", "banned"),
    )
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=28, null=False, choices=BLOG_STATUSES, default=BLOG_STATUSES[DRAFTED][0])
    title=models.CharField(max_length=1000, null=False)
    content=models.TextField(null=True)
    views=models.IntegerField(default=0)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"<Blog {self.title} by {self.author.username}>"