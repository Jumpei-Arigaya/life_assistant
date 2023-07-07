from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header

import time
import jwt
from config.settings import SECRET_KEY
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
    )


class JWTAuthentication(BaseAuthentication):
    """一般アカウント権限"""

    keyword = "JWT"
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        print(auth)
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = "Authorization 無効"
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = "Authorization 無効 スペースはない"
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt_token, SECRET_KEY, algorithms=["HS256"])
            userid = jwt_info.get("userid")
            try:
                user = User.objects.get(pk=userid)
                user.is_authenticated = True
                return (user, jwt_token)
            except:
                msg = "ユーザー存在しません"
                raise exceptions.AuthenticationFailed(msg)
        except jwt.ExpiredSignatureError:
            msg = "tokenはタイムアウトしました"
            raise exceptions.AuthenticationFailed(msg)

    def authenticate_header(self, request):
        pass
