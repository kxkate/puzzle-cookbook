from django.db import models
from django.contrib.auth.models import User
from accounts.models import MyUser

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


class FoodRecipe(models.Model):
    dish_title = models.CharField(max_length=128)
    dish_type = models.CharField(max_length=2, choices=FoodRecipeDishType.choices)
    preparation_time = models.IntegerField()
    ingredients = models.ManyToManyField(Ingredient, related_name="food_recipes")
    favourites = models.ManyToManyField(User, related_name="favourites", default=None, blank=True)


