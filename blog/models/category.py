from django.db import models

class CategoryModel(models.Model):
    """
    Represents a category in the database.

    Attributes:
        category (str): The name of the category.
    """

    category = models.CharField(max_length=128, unique=True)

    def __str__(self):
        """
        Returns a human-readable string representation of the category.

        Returns:
            str: A formatted string representing the category.
        """
        return f'{self.category}'
