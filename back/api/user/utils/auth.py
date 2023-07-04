import time
import jwt
from config.settings import SECRET_KEY
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from api.user.models import User


class NormalAuthentication(BaseAuthentication):
    """一般アカウント権限認証"""

    def authenticate(self, request):
        username = request._request.POST.get("username")
        password = request._request.POST.get("password")
        user_obj = User.objects.filter(username=username).first()
        if not user_obj:
            raise exceptions.AuthenticationFailed("認証失敗")
        elif user_obj.password != password:
            raise exceptions.AuthenticationFailed("認証失敗")
        token = generate_jwt(user_obj)
        return (token, None)

    def authenticate_header(self, request):
        pass


# jwtライブラリでTokenを生成
# Tokenの内容はユーザーの情報とタイムアウトが含まれている
# タイムアウトのキーはexpであることは固定
# ドキュメント: https://pyjwt.readthedocs.io/en/latest/usage.html?highlight=exp
def generate_jwt(user):
    timestamp = int(time.time()) + 60 * 60 * 24 * 7
    return jwt.encode(
        {
            "userid": user.pk,
            "username": user.username,
            "exp": timestamp,
        },
        SECRET_KEY,
    ).decode("utf-8")
