from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path("", views.home, name = 'home'),
	path("home/", views.home, name = 'home1'),
	path("register/", views.register, name = "register"),
	path("login/", views.login, name = "login"),
	path("contact/", views.contact, name = "contact page"),
	path("module/", views.module, name = "module"),
	path("logout/", views.logout, name = "logout"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)