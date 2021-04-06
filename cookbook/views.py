import requests
from django.shortcuts import render

def test(request):
    url = 'https://api.spoonacular.com/recipes/716429/information?includeNutrition=false&apiKey=1c11a4968bf74a0e9be0423f770f7f27'
    response = requests.get(url)
    print(response.text)
    return render(request, 'cookbook/index.html')

### do opracowania
#UsersChoice:
#     # wybór uzytkownika po kategoriach produktow:
#     # - mięso
#     # - warzywa
#     #- owoce itp
#     # po typie dania
#     # po czasie przygotowania
#     # po rodzaju kuchni
#     # jaki % skladnikow uzytkownik jest sklonny dokupic (views)