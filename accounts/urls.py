from django.urls import include, path
from . import views
import django.contrib.auth.urls
app_name = 'accounts'


urlpatterns = [
    path('', include(django.contrib.auth.urls)),
    # path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    # path('favourites/', views.favourite_list, name='favourite_list')
]


