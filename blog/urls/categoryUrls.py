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

# Import the view class that will handle the URL pattern
from blog.views.category.categoryView import CategoryView

# Define a list of URL patterns using the 'urlpatterns' variable
urlpatterns = [
    # Define a URL pattern using the 'path' function:
    # - The empty string ('') represents the URL path that this pattern will match.
    # - 'CategoryView.as_view()' specifies the view class that will handle this URL pattern and the request.
    #   '.as_view()' is used to convert the view class into a callable view function.
    # - This pattern maps to the root URL of your application, so when a user visits the root URL,
    path('', CategoryView.as_view())
]
