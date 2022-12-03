from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
	#return HttpResponse("<h1>home</h1>")
	return render(request, 'WebApp/home.html')

def register(request):
	return render(request, 'WebApp/register.html')

def login(request):
	return render(request, 'WebApp/login.html')

def contact(request):
	return HttpResponse("contact")

def resource(request):
	return HttpResponse("resource 1")
