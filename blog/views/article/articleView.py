#Importing the module APIView
from rest_framework.views import APIView
# Import the model and the serializer class
from blog.serializers.article import ArticleSerializer
from blog.models.article import ArticleModel
from blog.models.category import CategoryModel

# Importing the response module
from rest_framework.response import Response

# Import status module
from rest_framework import status

# Import Http404 exception
from django.http import Http404

# Import exception 'ValidationError'
from rest_framework.exceptions import ValidationError

class ArticleView(APIView):
    """ 
    Create and get objects from Article Table
    """

    def get_category(self, pk):
        """
        Retrieve a category Entity by its primary key (pk).

        Parameters:
        - pk (int): The primary key of the category to retrieve.

        Returns:
        CategoryModel: The CategoryModel instance with the specified primary key.

        Raises:
        Http404: If no category with the specified primary key is found.
        """
        try:
            return CategoryModel.objects.get(pk=pk)
        except CategoryModel.DoesNotExist:
            raise Http404

    def post(self, request):
        """
        Create a new article object and return a response.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        Response: HTTP response with a success message and the serialized data of the created object.

        Raises:
        ValidationError: If there are validation errors in the request data.
        """
        try:
            data = request.data
            serializer = ArticleSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            category = self.get_category(data.get("category"))
            serializer.save(category=category)
            return Response({'message': 'Object created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'message': 'Validation error', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Retrieve all articles and return a response.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        Response: HTTP response with serialized data of all articles.

        """
        articles = ArticleModel.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
