from api.recipe.views import RecipeList
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r"recipe_list", RecipeList, basename="recipe")

urlpatterns = [
    path("", include(router.urls)),
]
