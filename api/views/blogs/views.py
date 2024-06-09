from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from api.serializers.blogs import serializers
from rest_framework.decorators import permission_classes
from blogs.models import Blog
from rest_framework.permissions import IsAuthenticated
from blogs.services import BlogService
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from blogs.filters.api import BlogFilter

# Create your views here.
class GetBlogs(generics.ListAPIView):
    serializer_class = serializers.BlogSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BlogFilter
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']

    def get_queryset(self):
        return BlogService.get_all_blogs()

    def post(self, request):
        serializer_class= serializers.BlogSerializer
        serializer = serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @permission_classes([IsAuthenticated])
# class BlogFetchUpdateDeleteView(generics.GenericAPIView):
    
#     def get(self, request, blog_id):

#         serializer_class= serializers.MyBlogsSerializer

#         # Access the logged-in user
#         logged_in_user = request.user
#         try:
#             blog = Blog.objects.get(pk=blog_id)
#         except Blog.DoesNotExist:
#             return Response(data={"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
#         if request.user.is_superuser or request.user.is_admin:
#             serializer = serializers.AdminSerializer(blog, data=request.data, context={'request': request})
#         elif(logged_in_user.id != blog.sales_rep_id):
#             return Response(data={"error": "Blog does not belong to you"}, status=status.HTTP_403_FORBIDDEN)
        
#         serializer=serializer_class(instance=blog, many=False)
#         response={'message': "Blog found", 'data':serializer.data}
#         return Response(data=response, status=status.HTTP_200_OK)
    
#     def put(self, request, blog_id):
        
#         # Access the logged-in user
#         logged_in_user = request.user
#         try:
#             blog = Blog.objects.get(pk=blog_id)
#         except Blog.DoesNotExist:
#             return Response(data={"error": "Blog not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         if request.user.is_superuser or request.user.is_admin:
#             serializer = serializers.AdminSerializer(blog, data=request.data, context={'request': request})
#         elif(logged_in_user.id != blog.sales_rep_id):
#             return Response(data={"error": "Blog does not belong to you"}, status=status.HTTP_403_FORBIDDEN)
#         else:
#             serializer = serializers.MyBlogsSerializer(blog, data=request.data, context={'request': request})

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)