from django.db import models
from blog.models.category import CategoryModel

class ArticleModel(models.Model):
    """
    Represents an article in the database.

    Attributes:
        title (str): The title of the article, limited to 64 characters.
        subject (str): The subject or topic of the article, limited to 128 characters.
        content (str): The main content of the article, typically longer text.
        category (ForeignKey): A reference to the associated category using the CategoryModel.
    """

    title = models.CharField(max_length=64)
    subject = models.CharField(max_length=128)
    content = models.TextField()
    category = models.ForeignKey(CategoryModel, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a human-readable string representation of the article.

        Returns:
            str: A formatted string representing the article by its title.
        """
        return f"Article({self.title})"
