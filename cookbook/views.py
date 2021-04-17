import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from cookbook.forms import RecipeSearchForm
from django.views.decorators.csrf import csrf_exempt
from accounts.models import MyUser
from django.urls import reverse

from django.contrib.auth.models import User



def view_homepage(request):
    context = {'form': RecipeSearchForm()}
    return render(request, 'cookbook/homepage.html', context)


def search_recipes(request):
    form = RecipeSearchForm(request.POST or None)
    search_url = 'https://api.spoonacular.com/recipes/complexSearch'
    if form.is_valid():
        search_params = {
            'includeIngredients': ','.join(form.cleaned_data.get('ingredients')),
            'type': form.cleaned_data.get('dish_type'),
            'maxReadyTime': form.cleaned_data.get('max_preparation_time'),
            'number': '9',
            'apiKey': settings.SPOONACULAR_DATA_API_KEY
        }
        response = requests.get(search_url, params=search_params)
        results = response.json()
        recipes = []

        if not results['results']:
            return render(request, 'cookbook/no_recipe.html', {'recipes': recipes})
        for result in results['results']:
            recipe_data = {
                'dish_name': result['title'],
                'image': result['image'],
                'id': result['id'],
            }

            recipes.append(recipe_data)
        return render(request, 'cookbook/main_search.html', {'recipes': recipes})
    return render(request, 'cookbook/homepage.html', {'form': form})

@csrf_exempt
def show_recipe_details(request,id):  ## przepisac na get, przymuje argument id - parametr w url  + TEMPLATKA
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

@login_required
def add_favourites(request):
    id = request.POST.get('id')
    print(id)
    user1 = MyUser.objects.get(user=request.user)
    print(user1)
    user1.my_favourites.append(id)
    print(user1.my_favourites)
    user1.save()
    return HttpResponseRedirect(reverse('cookbook:recipes_details', kwargs={'id': id}))


    # recipe = get_object_or_404(FoodRecipe, id=id)
    # if recipe.id.filter(id=id).exists():
    #     pass
    # else:
    #     FoodRecipe.objects.create(dish_title="dish1", dish_type="breakfast", preparation_time=30,
    #                               ingredients=Ingredient.objects.get(ingredient_name='ahi tuna'),
    #                               favourites=User.objects.get(username="Kasia"))
    # if recipe.favourites.filter(id=request.user.id).exists():
    #     recipe.favourites.remove(request.user)
    # else:
    #     recipe.favourites.add(request.user)







def hello(request):
    return HttpResponse('ingredients')
