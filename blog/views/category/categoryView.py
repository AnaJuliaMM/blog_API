from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework import status
from blog.models.category import CategoryModel
from blog.serializers.category import CategorySerializer

class CategoryView(APIView):
    """
    Create and get objects from Category Table
    """

    def post(self, request):
        """
        Create a new category object and return a response.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        Response: HTTP response with a success message and the serialized data of the created object.

        Raises:
        ValidationError: If there are validation errors in the request data.
        """
        try:
            data = request.data
            serializer = CategorySerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'Object created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'message': 'Validation error', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Retrieve all categories and return a response.

        Parameters:
        - request (HttpRequest): The HTTP request object.

        Returns:
        Response: HTTP response with serialized data of all categories.

        """
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

