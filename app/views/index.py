from django.shortcuts import render
from app.models import Recipe


def index(req):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(req, 'index.html', context)
