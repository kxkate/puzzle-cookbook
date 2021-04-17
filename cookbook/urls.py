from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'cookbook'

urlpatterns = [
    path('', views.view_homepage, name='index'),
    path('recipes/', views.search_recipes, name='recipes_search'),
    path('recipes_details/<id>', views.show_recipe_details, name='recipes_details'),
    path('favourites_add', views.add_favourites, name='add_favourites')
]