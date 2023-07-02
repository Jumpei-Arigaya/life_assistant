# Serializerの例
from rest_framework import serializers
from api.recipe.models import *


class RecipeLargeCategorySerializer(serializers.ModelSerializer):
    """楽天レシピAPIの大カテゴリのシリアライザ"""

    categoryId = serializers.CharField(source="id")
    categoryName = serializers.CharField(source="name")
    categoryUrl = serializers.URLField(source="category_url")

    class Meta:
        model = RecipeLargeCategory
        fields = ["categoryId", "categoryName", "categoryUrl"]
