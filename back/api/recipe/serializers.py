from rest_framework import serializers
from api.recipe.models import *


class RecipeListSerializer(serializers.ModelSerializer):
    """レシピリストのシリアライザ"""

    class Meta:
        model = Recipe
        fields = "__all__"
