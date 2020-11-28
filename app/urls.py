from django.urls import path
from app.views.create import create_recipe
from app.views.delete import delete_recipe
from app.views.details import details_recipe
from app.views.edit import edit_recipe
from app.views.index import index

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:pk>/', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>/', delete_recipe, name='delete recipe'),
    path('details/<int:pk>/', details_recipe, name='details recipe')
]
