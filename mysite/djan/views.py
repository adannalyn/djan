from django.shortcuts import render

# Create your views here.

def djan(request):
	return render(request, "djan/index.html")

def about(request):
	return render(request, "djan/about.html")

def contact(request):
	return render(request, "djan/contact.html")

def services(request):
<<<<<<< HEAD
  return render(request, "djan/services.html")
=======
    return render(request, "djan/services.html")
>>>>>>> 0873b84cb8a08437bdf6362ac1f1860c06a5014a
