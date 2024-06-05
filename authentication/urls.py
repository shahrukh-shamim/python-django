from django.urls import path
from . import views
urlpatterns = [
    # path("", views.AuthView.as_view(), name="authIndex"),
    path("signup/", views.SignUpView.as_view(), name="signUpView"),
    path("login/", views.LoginView.as_view(), name="logInView"),
]