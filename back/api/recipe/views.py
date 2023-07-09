from django.shortcuts import render
from rest_framework import viewsets
from api.recipe.serializers import RecipeListSerializer
from api.recipe.models import *

# Create your views here.


class RecipeList(viewsets.ModelViewSet):
    """レシピモデルを操作するビューセット"""

    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
