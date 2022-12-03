from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name = 'home'),
	path("home/", views.home, name = 'home1'),
	path("register/", views.register, name = "register"),
	path("login/", views.login, name = "login"),
	path("contact/", views.contact, name = "contact page"),
	path("resource/", views.resource, name = "resource page 1"),

]