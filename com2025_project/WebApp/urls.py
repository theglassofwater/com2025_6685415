from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path("", views.home, name = 'home'),
	path("home/", views.home_loggedin, name = 'home1'),
	path("register/", views.register, name = "register"),
	path("login/", views.login, name = "login"),
	path("contact/", views.contact, name = "contact page"),
	path("course/", views.course, name = "course"),
	path("logout/", views.logout, name = "logout"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)