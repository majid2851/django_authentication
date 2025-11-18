from django.urls import path
from .views import Login
from .views import RegisterUser

urlpatterns =[
    path("login/",Login.as_view(), name="login"),
    path("register/",RegisterUser.as_view() ,name="register")
]