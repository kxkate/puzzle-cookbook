from django.db import models


class FoodRecipeDishType(models.TextChoices):
    BREAKFAST = 'BF', 'breakfast'
    SALAD = 'SD', 'salad'
    APPETIZER = 'AP', 'appetizer'
    SOUP = 'SP', 'soup'
    MAIN_COURSE = 'MC', 'main course'
    DESSERT = 'DS', 'dessert'


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=128)

    def __str__(self):
        return self.ingredient_name



