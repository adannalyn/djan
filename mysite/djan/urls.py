from django.urls import path
from .views import djan, about, contact, services

app_name = "djan"

urlpatterns = [
    
    path("", djan, name="djanView"),
    path("about/", about, name="aboutView"),
    path("contact/", contact, name="contactView"),
    path("services/", services, name="servicesView")
    
]
