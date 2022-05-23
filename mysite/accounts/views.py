from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def signup(request):
  return HttpResponse("<p> SignUp here</p>")
  
def login(request):
  return HttpResponse("<p> Login here </p>")
