from django.urls import path
from .views import signup, login
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("", signup, name="signupView"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="loginView"),
    path("login/", auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logoutView"),
]