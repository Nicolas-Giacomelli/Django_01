from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from recipes.models import Recipe
# Create your views here.

def home(request):
    recipes = Recipe.objects.all().order_by('-id')
=======
from utils.recipes.factory import make_recipe
from django.http import Http404

from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
>>>>>>> c976c6b (Aula_62)
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })

<<<<<<< HEAD
=======

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')
    
    if not recipes:
        raise Http404('Not Found :C')
    
    
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{category_name} - Category'
    })


>>>>>>> c976c6b (Aula_62)
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
<<<<<<< HEAD

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id
        ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes':recipes,
    })
=======
>>>>>>> c976c6b (Aula_62)
