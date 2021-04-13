from django import forms
from django.forms import CharField, Form, IntegerField,ChoiceField, Textarea
from django.contrib.admin.widgets import FilteredSelectMultiple


DISH_TYPE_CHOICES =(
    ("breakfast", "Breakfast"),
    ("salad", "Salad"),
    ("appetizer", "Appetizer"),
    ("soup", "Soup"),
    ("main course", "Main course"),
    ("dessert", "Dessert"),
    ("", "All Types")
)


class RecipeSearchForm(Form):
    ingredients = CharField(max_length=200)
    dish_type = ChoiceField(choices=DISH_TYPE_CHOICES,required=False)
    max_preparation_time = IntegerField(help_text='minutes', required=False,
                                        widget=forms.TextInput(attrs={'placeholder': 'Field not required'}))




