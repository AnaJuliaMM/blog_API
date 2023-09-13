from rest_framework import serializers
from blog.models.category import CategoryModel
from blog.serializers.article import ArticleSerializer

class CategorySerializer(serializers.ModelSerializer):
    categories = ArticleSerializer(read_only=True,many=True)
    class Meta:
        model = CategoryModel
        fields = "__all__"