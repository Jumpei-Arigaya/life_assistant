from django.contrib import admin
from api.recipe.models import *

# Register your models here.
admin.site.register(
    [RecipeLargeCategory, RecipeMediumCategory, RecipeSmallCategory, Recipe]
)
