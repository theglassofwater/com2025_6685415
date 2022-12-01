from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(response):
	return HttpResponse("home")


def contact(response):
	return HttpResponse("contact")

def resource(response):
	return HttpResponse("resource 1")
