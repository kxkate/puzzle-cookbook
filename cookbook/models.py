from django.db import models
from django.contrib.auth.models import User

class IngredientCategoryChoices(models.TextChoices):
    pass

class FoodRecipeCuisineType(models.TextChoices):
    pass

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=128)
    category = models.CharField(max_length=128) # choicefield
    kcal_value_100g = models.FloatField()

    def __str__(self):
        return self.ingredient_name


class FoodRecipe(models.Model):
    dish_name = models.CharField(max_length=128)
    dish_type = models.CharField(max_length=10)  #choicefield
    cuisine_type = models.CharField(max_length=128)
    preparation_time = models.IntegerField()  # info (sek, min)
    servings_number = models.IntegerField() # choicefield
    # ingredients = models.ManyToManyField(Ingredient, related_name="food_recipes")
    description = models.TextField()
    user_profiles = models.ManyToManyField(User, related_name="users")

    def __str__(self):
        return self.dish_name

    @property
    def calculate_kcal_value(self):
        pass


class FoodRecipeIngredient(models.Model):
    amount = models.IntegerField()
    unit = models.CharField(max_length=10) # choicefield
    ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(FoodRecipe, on_delete=models.CASCADE, related_name="ingredients")

