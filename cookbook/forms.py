from django import forms
from django.forms import CharField, Form, IntegerField,ChoiceField, MultipleChoiceField
from cookbook.models import Ingredient
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import FilteredSelectMultiple


DISH_TYPE_CHOICES = (
    ("breakfast", "Breakfast"),
    ("salad", "Salad"),
    ("appetizer", "Appetizer"),
    ("soup", "Soup"),
    ("main course", "Main course"),
    ("dessert", "Dessert"),
    ("", "All Types")
)

result = []
for ingredient in Ingredient.objects.all():
    result.append((ingredient.ingredient_name, ingredient.ingredient_name))

INGREDIENT_CHOICES = result


class MyIntegerField(IntegerField):
    default_error_messages = {
        'invalid': 'Enter the maximum preparation time in whole minutes!',
    }


class RecipeSearchForm(Form):
    ingredients = MultipleChoiceField(widget=forms.SelectMultiple, choices=INGREDIENT_CHOICES)
    dish_type = ChoiceField(choices=DISH_TYPE_CHOICES, required=False)
    max_preparation_time = MyIntegerField(help_text='minutes', required=False,
                                        widget=forms.TextInput(attrs={'placeholder': 'Field not required'}))

