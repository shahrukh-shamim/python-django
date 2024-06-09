# services.py
from .models import Blog

class BlogService:
    @staticmethod
    def get_all_blogs(filters=[]):
        return Blog.objects.all_blogs()