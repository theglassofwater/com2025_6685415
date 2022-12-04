from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import courses,users,modules,user_modules
from .forms import register_user
# Create your views here.


def home(request):

	return render(request, 'WebApp/home.html', {})

def register(request):
	if request.method == "POST":
		register_data = register_user(request.POST)

		if register_data.is_valid():
			fname = register_data.cleaned_data["fname"]
			lname = register_data.cleaned_data["lname"]
			username = register_data.cleaned_data["username"]
			password = register_data.cleaned_data["password"]
			email = register_data.cleaned_data["email"]
			course = register_data.cleaned_data["course"]
			user_data = users(fname=fname,lname=lname,username=username,password=password,email=email,course=course)
			user_data.save()
			return HttpResponseRedirect("/home")

	else:
		register_data = register_user()
	return render(request, 'WebApp/register.html', {"form":register_data})

def login(request):
	return render(request, 'WebApp/login.html', {})

def contact(request):
	return HttpResponse("contact")

def resource(request):
	return HttpResponse("resource 1")
