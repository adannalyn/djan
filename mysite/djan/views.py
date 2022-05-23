from django.shortcuts import render

# Create your views here.

def polls(request):
	return render(request, "polls.html")

def register(request):
	return render(request, "Register.html")

def vote(request):
	return render(request, "vote.html")
