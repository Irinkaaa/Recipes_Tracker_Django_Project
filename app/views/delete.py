from django.shortcuts import redirect, render
from app.forms.delete import DeleteRecipeForm
from app.models import Recipe


def delete_recipe(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    if req.method == 'GET':
        context = {
            'recipe': recipe,
            'form': DeleteRecipeForm(instance=recipe),
        }
        return render(req, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')
