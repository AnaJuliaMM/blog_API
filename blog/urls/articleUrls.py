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
from django.urls import path

# Import the view class that will handle the URL pattern
from blog.views import ArticleView

# Define a list of URL patterns using the 'urlpatterns' variable
urlpatterns = [
    # Define a URL pattern using the 'path' function:
    # - The empty string ('') represents the URL path that this pattern will match.
    # - 'ArticleView.as_view()' specifies the view class that will handle this URL pattern and will ne invoked to handle the request.
    #   '.as_view()' is used to convert the view class into a callable view function.
    path('', ArticleView.as_view())
]

