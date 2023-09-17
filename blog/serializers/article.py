# Import the necessary serializers module and the ArticleModel from your application
from rest_framework import serializers
from blog.models.article import ArticleModel

# Define a serializer class for the ArticleModel
class ArticleSerializer(serializers.ModelSerializer):
    # Create a field named 'category' using the StringRelatedField serializer field.
    # This field will represent the 'category' relationship as a string and is read-only.
    category = serializers.StringRelatedField(read_only=True)

    # Meta class is used to configure the serializer's behavior
    class Meta:
        # Specify the model that this serializer is associated with.
        model = ArticleModel

        # Use "__all__" to indicate that all fields from the ArticleModel should be included in the serializer.
        # This will include all model fields as well as any extra fields or methods defined in the model.
        fields = "__all__"
