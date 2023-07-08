from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from api.user.utils.auth import JWTAuthentication
from .utils.auth import NormalAuthentication


class Login(APIView):
    """JWTライブラリを使用したログイン認証処理"""

    authentication_classes = [
        NormalAuthentication,
    ]

    def post(self, request, *args, **kwargs):
        return Response({"token": request.user}, status=status.HTTP_200_OK)


class Something(APIView):
    # authentication_classes = [
    #     JWTAuthentication,
    # ]
    # # ログインユーザーのみアクセスを許可
    # permission_classes = [
    #     IsAuthenticated,
    # ]

    def get(self, request, *args, **kwargs):
        return Response({"data": "中身です"})
