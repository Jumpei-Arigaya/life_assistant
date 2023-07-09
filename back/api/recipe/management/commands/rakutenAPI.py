from django.core.management.base import BaseCommand
from api.recipe.models import *
from datetime import datetime
import requests
import os
import time


class Command(BaseCommand):
    """楽天レシピAPIからレシピに関するデータを取得してDBに保存"""

    def __init__(self):
        super().__init__()
        self.__RAKUTEN_API_KEY = os.getenv("RAKUTEN_API_KEY")
        self.__RAKUTEN_RECIPE_CATEGORY_URL = os.getenv("RAKUTEN_RECIPE_CATEGORY_URL")
        self.__RAKUTEN_RECIPE_URL = os.getenv("RAKUTEN_RECIPE_URL")

    def handle(self, *args, **options):
        """楽天レシピAPIからレシピに関するデータを取得してDBに保存するコマンドを実行"""

        self.__get_recipe_category()
        self.__get_recipe()

    def __get_recipe_category(self, *args, **options):
        """楽天レシピAPIからカテゴリを取得してDBに保存

        TODO 差分を更新する方式に変更
        """
        try:
            RecipeLargeCategory.objects.all().delete()
            RecipeMediumCategory.objects.all().delete()
            RecipeSmallCategory.objects.all().delete()

            response = requests.get(
                f"{self.__RAKUTEN_RECIPE_CATEGORY_URL}applicationId={self.__RAKUTEN_API_KEY}"
            )

            recipe_category = response.json()
            recipe_large_category_list = []
            recipe_medium_category_list = []
            recipe_small_category_list = []

            for large in recipe_category["result"]["large"]:
                recipe_large_category_list.append(
                    RecipeLargeCategory(
                        id=large["categoryId"],
                        name=large["categoryName"],
                        category_url=large["categoryUrl"],
                    )
                )
            RecipeLargeCategory.objects.bulk_create(recipe_large_category_list)

            for medium in recipe_category["result"]["medium"]:
                parent_category = RecipeLargeCategory.objects.get(
                    id=medium["parentCategoryId"]
                )
                recipe_medium_category_list.append(
                    RecipeMediumCategory(
                        id=medium["categoryId"],
                        name=medium["categoryName"],
                        category_url=medium["categoryUrl"],
                        parent_category=parent_category,
                    )
                )
            RecipeMediumCategory.objects.bulk_create(recipe_medium_category_list)

            for small in recipe_category["result"]["small"]:
                parent_category = RecipeMediumCategory.objects.get(
                    id=small["parentCategoryId"]
                )
                recipe_small_category_list.append(
                    RecipeSmallCategory(
                        id=small["categoryId"],
                        name=small["categoryName"],
                        category_url=small["categoryUrl"],
                        parent_category=parent_category,
                    )
                )
            RecipeSmallCategory.objects.bulk_create(recipe_small_category_list)
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")

    def __get_recipe(self, *args, **options):
        """楽天レシピAPIからカテゴリを取得してDBに保存

        TODO 差分を更新する方式に変更
        """

        Recipe.objects.all().delete()
        large_category_ids = list(
            RecipeLargeCategory.objects.values_list("id", flat=True)
        )
        for i in large_category_ids:
            time.sleep(2)
            try:
                response = requests.get(
                    f"{self.__RAKUTEN_RECIPE_URL}categoryId={i}&applicationId={self.__RAKUTEN_API_KEY}"
                )
                recipe = response.json()
                for recipe_data in recipe["result"]:
                    recipe_publishday_str = recipe_data["recipePublishday"]
                    recipe_publishday = datetime.strptime(
                        recipe_publishday_str, "%Y/%m/%d %H:%M:%S"
                    )
                    obj, created = Recipe.objects.update_or_create(
                        id=recipe_data["recipeId"],
                        defaults={
                            "name": recipe_data["recipeTitle"],
                            "recipe_url": recipe_data["recipeUrl"],
                            "food_image_url": recipe_data["foodImageUrl"],
                            "medium_image_url": recipe_data["mediumImageUrl"],
                            "small_image_url": recipe_data["smallImageUrl"],
                            "pickup": recipe_data["pickup"],
                            "shop": recipe_data["shop"],
                            "nick_name": recipe_data["rank"],
                            "recipe_description": recipe_data["recipeDescription"],
                            "recipe_materials": recipe_data["recipeMaterial"],
                            "recipe_indication": recipe_data["recipeIndication"],
                            "recipe_cost": recipe_data["recipeCost"],
                            "recipe_publishday": recipe_publishday,
                            "recipe_rank": recipe_data["rank"],
                        },
                    )
            except requests.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:
                print(f"Other error occurred: {err}")
