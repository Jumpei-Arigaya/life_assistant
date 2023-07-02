from django.db import models
from django.contrib.postgres.fields import ArrayField


class RecipeLargeCategory(models.Model):
    """楽天レシピAPIの大カテゴリ"""

    name = models.CharField(max_length=255)
    category_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RecipeMediumCategory(models.Model):
    """楽天レシピAPIの中カテゴリ"""

    name = models.CharField(max_length=255)
    category_url = models.URLField()
    parent_category = models.ForeignKey(RecipeLargeCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RecipeSmallCategory(models.Model):
    """楽天レシピAPIの小カテゴリ"""

    name = models.CharField(max_length=255)
    category_url = models.URLField()
    parent_category = models.ForeignKey(RecipeMediumCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Recipe(models.Model):
    """楽天レシピAPIのレシピ"""

    name = models.CharField(max_length=255)
    recipe_url = models.URLField()
    food_image_url = models.URLField()
    medium_image_url = models.URLField()
    small_image_url = models.URLField()
    pickup = models.CharField(max_length=3)
    shop = models.CharField(max_length=3)
    nick_name = models.CharField(max_length=255)
    recipe_description = models.TextField()
    recipe_materials = ArrayField(
        models.CharField(max_length=255), blank=True, null=True
    )  # 楽天レシピAPIから材料の配列が返されるためPostgreSQLのArrayFieldを使用
    recipe_indication = models.CharField(max_length=255)
    recipe_cost = models.CharField(max_length=255)
    recipe_publishday = models.DateTimeField()
    recipe_rank = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
