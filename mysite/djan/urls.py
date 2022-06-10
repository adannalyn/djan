from django.urls import path
from .views import polls, register, vote

app_name = "djan"

urlpatterns = [
    path("home/home", polls),
    path("home/about/", register),
    path("home/contact", vote)
]