import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from cookbook.forms import RecipeSearchForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User



def view_homepage(request):
    context = {'form': RecipeSearchForm()}
    return render(request, 'cookbook/homepage.html', context)


def search_recipes(request):
    form = RecipeSearchForm(request.POST or None)
    search_url = 'https://api.spoonacular.com/recipes/complexSearch'
    recipe_url = 'https://api.spoonacular.com/recipes/informationBulk'
    if form.is_valid():
        search_params = {
            'includeIngredients': form.cleaned_data.get('ingredients'),
            'type': form.cleaned_data.get('dish_type'),
            'maxReadyTime': form.cleaned_data.get('max_preparation_time'),
            'number': '9',
            'apiKey': settings.SPOONACULAR_DATA_API_KEY
        }

        response = requests.get(search_url, params=search_params)
        results = response.json()
        recipes = []

        if not results['results']:
            return render(request, 'cookbook/no_recipe.html', {'recipes':recipes})
        for result in results['results']:
            recipe_data = {
                'dish_name': result['title'],
                'image': result['image'],
                'id': result['id'],
            }

            recipes.append(recipe_data)
        return render(request, 'cookbook/main_search.html', {'recipes':recipes})


@csrf_exempt
def show_recipe_details(request):
    id = request.POST.get('id')
    details_url = f'https://api.spoonacular.com/recipes/{id}/information'
    search_params = {
        'apiKey': settings.SPOONACULAR_DATA_API_KEY
    }
    response = requests.get(details_url, params=search_params)
    result = response.json()
    ingredients_list = []
    for ingredient in result['extendedIngredients']:
        ingredient_data = {
            'name': ingredient['nameClean'],
            'amount': round(ingredient['amount'], 2),
            'unit': ingredient['measures']['metric']['unitShort']
        }
        ingredients_list.append(ingredient_data)

    steps_list = []
    for instruction in result['analyzedInstructions']:
        for step in instruction['steps']:
            step_data = {
                'step': step['step']
            }
            steps_list.append(step_data)

    recipe_det = {
        'id': result['id'],
        'title': result['title'],
        'image': result['image'],
        'prep_time': result['readyInMinutes'],
        'instructions': result['instructions'],
        'data': ingredients_list
    }

    return render(request, 'cookbook/recipe_details.html', {
        'recipe_det': recipe_det,
        'ingredients_list': ingredients_list,
        'steps_list': steps_list,
    })


def hello(request):
    return HttpResponse('ingredients')
