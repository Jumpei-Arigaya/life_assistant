from api.user.views import Login, Something
from django.urls import path

urlpatterns = [path("login/", Login.as_view()), path("data/", Something.as_view())]
