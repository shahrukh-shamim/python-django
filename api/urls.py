from django.urls import path
from .views.blogs import views as BlogViews
urlpatterns = [

    #Blog
    path("blogs/", BlogViews.GetBlogs.as_view(), name="BlogIndex")
]