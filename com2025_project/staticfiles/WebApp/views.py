from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import courses,users,modules,user_modules
from .forms import register_user,login_user
# Create your views here.


def home(request):
	context = {}
	context["course"] = request.session.get('course')
	return render(request, 'WebApp/home.html', context)

def register(request):
	context = {}
	if request.method == "POST":
		register_data = register_user(request.POST)

		if register_data.is_valid():
			fname = register_data.cleaned_data["fname"]
			lname = register_data.cleaned_data["lname"]
			username = register_data.cleaned_data["username"]
			password = register_data.cleaned_data["password"]
			email = register_data.cleaned_data["email"]
			course = register_data.cleaned_data["course"]
			if not users.objects.filter(username=username):
				user_data = users(fname=fname,lname=lname,username=username,password=password,email=email,course=course)
				user_data.save()
				username_id = users.objects.get(username=username) #register_data.cleaned_data["username"].id
				request.session['id'] = username_id.id
				request.session['course'] = username_id.course.name
				return HttpResponseRedirect("/home")
			else:
				context["incorrect"] = "Username already taken"


	
	register_data = register_user()
	context["form"] = register_data

	return render(request, 'WebApp/register.html', context)

def login(request):
	context = {}
	if request.method == "POST":
		login_data = login_user(request.POST)
		if login_data.is_valid():
			username = login_data.cleaned_data["username"]
			password = login_data.cleaned_data["password"]
			if users.objects.filter(username=username):
				user_data = users.objects.get(username=username)
				if user_data.get_password() == password:
					request.session["id"] = user_data.id
					request.session["course"] = user_data.course.name
					return HttpResponseRedirect("/home")
				else:
					context["incorrect"] = "Password does not match username"
			else:
				context["form"] = login_data
				context["incorrect"] = "Username does not exist"

	
	login_data = login_user()
	context["form"] = login_data
	return render(request, 'WebApp/login.html', context)

def contact(request):
	return HttpResponse("contact")

def module(request):
	return HttpResponse("module")
