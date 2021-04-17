from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from cookbook.models import Ingredient
from django.contrib.auth.models import User


from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordChangeDoneView, PasswordResetView,
                                       PasswordResetDoneView,PasswordResetConfirmView,
                                       PasswordResetCompleteView)



