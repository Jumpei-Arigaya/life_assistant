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
        """JWTライブラリを使用したログイン認証処理

        Args:
            request (object): フォームに入力されたユーザー情報
        """
        try:
            response = Response({"token": request.user}, status=status.HTTP_200_OK)
            response.set_cookie(
                "token",
                request.user,
                httponly=True,
                secure=True,
                max_age=60 * 60 * 24,
            )
        except Exception as e:
            print(str(e))
            return Response(
                {"error": "Something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return response


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
