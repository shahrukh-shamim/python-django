from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from api.serializers.blogs import serializers
from rest_framework.decorators import permission_classes
from blogs.models import Blog
from rest_framework.permissions import IsAuthenticated
from blogs.services import BlogService

# Create your views here.
class GetBlogs(generics.GenericAPIView):
    serializer_class = serializers.BlogSerializer

    def get(self, request):
        # # Access the logged-in user
        # logged_in_user = request.user
        
        filters =  request.filters if hasattr(request, 'filters') else []
        print(request)  
        blogs = BlogService.get_all_blogs(filters)
        
        serializer = self.get_serializer(instance=blogs, many=True)
        data = { "message": "All orders", "data": serializer.data }
        return Response(data=data, status=status.HTTP_200_OK)
    
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