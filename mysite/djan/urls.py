from django.urls import path
from .views import djan, about, contact, services

app_name = "djan"

urlpatterns = [
    
    path("", djan, name="djanView"),
    path("about/", about, name="aboutView"),
    path("contact/", contact, name="contactView"),
    path("services/", services, name="servicesView")
    
<<<<<<< HEAD
]
=======
]
>>>>>>> 0873b84cb8a08437bdf6362ac1f1860c06a5014a
