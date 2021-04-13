from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from cookbook.models import FoodRecipe


from django.contrib.auth.views import (LoginView, PasswordChangeView,
                                       PasswordChangeDoneView, PasswordResetView,
                                       PasswordResetDoneView,PasswordResetConfirmView,
                                       PasswordResetCompleteView)

# @login_required
# def favourite_list(request):
#     new = FoodRecipe.objects.filter(favourites=request.user)
#     return render(request,
#                   'accounts/favourites.html',
#                   {'new':new})
#
#
# @login_required
# def favourite_add(request, id):
#     id = request.POST.get('id')
#     recipe = get_object_or_404(FoodRecipe, id=id)
#     if recipe.objects.filter(id=request.user.id).exists():
#         recipe.favourites.remove(request.user)
#     else:
#         recipe.favourites.add(request.user)
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])