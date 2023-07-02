from django.core.management.base import BaseCommand
from api.recipe.serializer import *
import requests
import os


class Command(BaseCommand):
    """楽天レシピAPIからレシピデータを取得してDBに保存する"""

    def handle(self, *args, **options):
        self.__RAKUTEN_API_KEY = os.getenv("RAKUTEN_API_KEY")
        self.__RAKUTEN_RECIPE_CATEGORY_URL = os.getenv("RAKUTEN_RECIPE_CATEGORY_URL")

        response = requests.get(
            f"{self.__RAKUTEN_RECIPE_CATEGORY_URL}{self.__RAKUTEN_API_KEY}"
        )
        data = response.json()
        serializer = RecipeLargeCategorySerializer(
            data=data["result"]["large"], many=True
        )
        if serializer.is_valid():
            serializer.save()
        else:
            # print(data["result"]["large"])
            print(serializer.errors)
