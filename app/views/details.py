from django.shortcuts import render
from django.views.decorators.http import require_GET
from app.forms.create import RecipeForm
from app.models import Recipe


@require_GET
def details_recipe(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = str(recipe.ingredients)
    context = {
        'recipe': recipe,
        'ingredients': ingredients.split(','),
        'form': RecipeForm(instance=recipe),
    }
    return render(req, 'details.html', context)
