from django.urls import path
from .views import home, about, contact

app_name = "home"

urlpatterns = [
	path("", home, name="homeView"),
    path("about/", about, name="aboutView"),
    path("contact/", contact, name="contactView")
]
