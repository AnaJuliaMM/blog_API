from rest_framework import serializers
# Import the necessary serializers module and the CategoryModel and ArticleSerializer
# from your application
from rest_framework import serializers
from blog.models.category import CategoryModel
from blog.serializers.article import ArticleSerializer

# Define a serializer class for the CategoryModel
class CategorySerializer(serializers.ModelSerializer):
    # Create a field named 'articles' using the ArticleSerializer.
    # This field represents the reverse relationship from CategoryModel to ArticleModel.
    # 'many=True' indicates that multiple articles can be associated with a category.
    # 'read_only=True' specifies that this field is read-only and won't be used for deserialization.
    articles = ArticleSerializer(many=True, read_only=True)

    # Meta class is used to configure the serializer's behavior
    class Meta:
        # Specify the model that this serializer is associated with.
        model = CategoryModel

        # Use "__all__" to indicate that all fields from the CategoryModel should be included in the serializer.
        # This includes all database fields and any additional fields or methods defined in the model.
        fields = "__all__"
