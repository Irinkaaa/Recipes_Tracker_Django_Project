from django.shortcuts import render, redirect
from app.forms.create import RecipeForm
from app.models import Recipe


def edit_recipe(req, pk):
    recipe = Recipe.objects.get(pk=pk)
    if req.method == 'GET':
        context = {
            'recipe': recipe,
            'form': RecipeForm(instance=recipe),
        }
        return render(req, 'edit.html', context)
    else:
        form = RecipeForm(req.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'recipe': recipe,
                'form': form,
            }
            return render(req, 'edit.html', context)
