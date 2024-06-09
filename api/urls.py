from django.urls import path
from .views.blogs import views as BlogViews
urlpatterns = [

    #Blog
    path("blogs/", BlogViews.BlogListCreateView.as_view(), name="BlogListCreateView"),
    path('blogs/<int:pk>/', BlogViews.BlogDetailView.as_view(), name='BlogDetailView'),
]