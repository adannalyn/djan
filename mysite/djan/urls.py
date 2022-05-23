from django.urls import path
from .views import polls, register, vote

urlpatterns = [
    path("polls/", polls),
    path("register/", register),
    path("vote/", vote)
]