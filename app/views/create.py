from django.shortcuts import render, redirect
from app.forms.create import RecipeForm


def create_recipe(req):
    if req.method == 'GET':
        context = {
            'form': RecipeForm(),
        }
        return render(req, 'create.html', context)
    else:
        form = RecipeForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(req, 'create.html', context)
