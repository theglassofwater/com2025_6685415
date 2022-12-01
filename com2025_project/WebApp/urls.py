from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name = 'home'),
	path("home", views.home, name = 'home'),
	path("contact", views.contact, name = "contact page"),
	path("resource", views.resource, name = "resource page 1")

]