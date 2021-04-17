from django.urls import include, path
from . import views
import django.contrib.auth.urls
app_name = 'accounts'


urlpatterns = [
    path('', include(django.contrib.auth.urls)),
    # path('favourites/', views.favourite_list, name='favourite_list')
]


