"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import the necessary modules from Django
from django.contrib import admin
from django.urls import path, include

# Define the URL patterns for your Django application
urlpatterns = [
    # Admin URL: Access the Django admin interface
    path('admin/', admin.site.urls),

    # Articles URL: Include URL patterns from the 'blog.urls.articleUrls' module
    # These patterns are used to handle article-related endpoints
    path('articles', include('blog.urls.articleUrls')),

    # Categories URL: Include URL patterns from the 'blog.urls.categoryUrls' module
    # These patterns are used to handle category-related endpoints
    path('categories', include('blog.urls.categoryUrls'))
]

