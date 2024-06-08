from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('cms/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('auth/', include('djoser.urls.jwt')),

    #WEB routes 
    path('blogs/', include('blogs.urls')),

    #SESSION BASED URLS
    path('', include('authentication.sessionbased_authentication_urls')),

    #HOME URL
    path('', include('home.urls')),
]
