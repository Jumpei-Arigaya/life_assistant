from rest_framework.views import APIView
from rest_framework.response import Response

from .utils.auth import NormalAuthentication


class Login(APIView):
    """JWTライブラリを使用したログイン認証処理"""

    authentication_classes = [
        NormalAuthentication,
    ]

    def post(self, request, *args, **kwargs):
        return Response({"token": request.user})
