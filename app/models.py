from django.db import models
from app.validators import ingredients_validator


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=30)
    image_url = models.URLField()
    description = models.TextField()
    ingredients = models.CharField(
        max_length=250,
        validators=(
            ingredients_validator,
        )
    )
    time = models.IntegerField()

    def __str__(self):
        return f'{self.title}'
