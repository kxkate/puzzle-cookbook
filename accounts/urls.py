from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

app_name = 'accounts'


urlpatterns = [
    path('my-login/', auth_views.LoginView.as_view(template_name="registration/login.html",
                                                authentication_form=UserLoginForm), name='mylogin'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('register/', views.accounts_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>)/',
         views.activate, name='activate'),
    # path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    # path('favourites/', views.favourite_list, name='favourite_list')
]


