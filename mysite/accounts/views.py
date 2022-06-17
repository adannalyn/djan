from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
        else:
            pass 
    
    context = {
        "name": "Saviuor Bassey",
        "gender": "male",
        "email": "user@gmail.com",
        "form": UserCreationForm()
    }
    return render(request, "accounts/django-register.html", context)

def login(request):
    return HttpResponse("<b> login here </b>")
