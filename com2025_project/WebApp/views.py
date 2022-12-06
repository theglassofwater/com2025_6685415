from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from .models import courses,users,modules,user_modules
from .forms import register_user,login_user,ContactForm,modules_form
from django.core.mail import send_mail, BadHeaderError 
from django.contrib import messages 

# Create your views here.

def logout(request):
	request.session.flush()
	return render(request, 'WebApp/home.html')

def home(request):
	context = {}
	if request.session.get('id') == None:
		return render(request, 'WebApp/home.html', context)
	context["course"] = request.session.get('course')
	context["logout"] = "Log out"
	return render(request, 'WebApp/home_loggedin.html', context)


def home_loggedin(request):
	context = {}
	if request.session.get('id') == None:
		return render(request, 'WebApp/home.html', context)
	context["course"] = request.session.get('course')
	context["logout"] = "Log out"
	return render(request, 'WebApp/home_loggedin.html', context)


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
				request.session["logged_in"] = "Logout"
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
					request.session["logged_in"] = "Logout"
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
	context = {}
	if request.session.get('id') == None:
		context["signin"] = "You must sign in before trying to contact us"
		return render(request, 'WebApp/home.html', context)
	if request.method == "GET":
		form = ContactForm() 
	else:
		form = ContactForm(request.POST) 
		if form.is_valid(): 
			name = form.cleaned_data['name'] 
			subject = form.cleaned_data['subject'] 
			email = form.cleaned_data['email'] 
			message = name + ':\n' + form.cleaned_data['message'] 
			try: 
				send_mail(subject, message, email, ['myemail@mydomain.com'])
			except BadHeaderError: 
				messages.add_message(request, messages.ERROR, 'Message Not Sent') 
				return HttpResponse("Invalid header found.") 

			messages.add_message(request, messages.SUCCESS, 'Message Sent')
			return redirect(reverse('home'))
		else:
			messages.add_message(request, messages.ERROR, 'Invalid Form Data; Message Not Sent') 
	context["course"] = request.session.get('course')
	context["logout"] = "Log out"
	context["form"] = form
	return render(request, 'WebApp/contact.html', context) 


def course(request):
	context = {}
	if request.method == "POST":
		course_data = modules_form(request.POST)

		if course_data.is_valid():
			modules = []
			credits=0
			for i in range(1,5):
				
				modules.append(course_data.cleaned_data["module"+str(i)])
				credits = credits + modules[i-1].credits
			#if not users.objects.filter(username=username):

			if credits > 80:
				context["incorrect"] = "Too many credits selected and atleast 3 modules must be selected"
				context["course"] = request.session.get('course')
				context["logout"] = "Log out"
				context["form"] = modules_form()
				return render(request, 'WebApp/course.html', context)

			for module in modules:
				module_user = user_modules(user= users.objects.get(id=request.session.get("id")), module = module)
				module_user.save()
			return HttpResponseRedirect("/home")
		else:
			context["incorrect"] = "Too many credits selected and atleast 3 modules must be selected"

	#context = {}
	context["course"] = request.session.get('course')
	context["logout"] = "Log out"
	context["form"] = modules_form()
	return render(request, 'WebApp/course.html', context)
