from django.test import TestCase, Client
from django.urls import reverse
from .models import users,modules,courses,user_modules
# Create your tests here.


class ViewsTests(TestCase):

	def setUp(self):
		self.client = Client()
		self.home_url = reverse("home1")
		self.register_url = reverse("register")
		self.login_url = reverse("login")
		self.contact_url = reverse("contact page")
		self.course_url = reverse("course")
		self.logout_url = reverse("logout")

	def test_home(self):
		response = self.client.get(self.home_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "WebApp/home.html")
	def test_register(self):
		response = self.client.get(self.register_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "WebApp/register.html")
	def test_login(self):
		response = self.client.get(self.login_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "WebApp/login.html")
	def test_contact(self):
		response = self.client.get(self.contact_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "WebApp/home.html")
	def test_course(self):
		response = self.client.get(self.course_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "WebApp/course.html")
	def test_logout(self):
		response = self.client.get(self.logout_url)
		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, "WebApp/home.html")





class modelTests(TestCase):

	def setUp(self):
		pass

	def test_models_creation(self):
		course = courses(name = "Maths")

		user = users(fname="Youssef",lname="el-aasar",username="hello",password="hello",course=course)
		module = modules(name="Integration",course=course)
		user_module = user_modules(user=user,module=module)
		course.save()
		user.save()
		module.save()
		user_module.save()

	def test_duplicates(self):
		course = courses(name = "Maths")
		course2 = courses(name= "Maths")
		user = users(fname="Youssef",lname="el-aasar",username="hello",password="hello",course=course)
		user2 = users(fname="Yousef",lname="el-asar",username="hello",password="helloo",course=course)
		module = modules(name="Integration",course=course)
		module2 = modules(name="Integration", course=course)
		user_module = user_modules(user=user,module=module)
		user_module2 = user_modules(user=user, module=module)
		course.save()
		try:
			with transaction.atomic():
				course2.save()
		except Exception:
			pass
		self.assertEquals(courses.objects.all().count(), 1)

		user.save()
		try:
			with transaction.atomic():
				user2.save()
		except Exception:
			pass
		self.assertEquals(users.objects.all().count(), 1)

		module.save()
		try:
			with transaction.atomic():
				module2.save()
		except Exception:
			pass
		self.assertEquals(modules.objects.all().count(), 1)

		user_module.save()
		try:
			with transaction.atomic():
				user_module2.save()
		except Exception:
			pass
		self.assertEquals(user_modules.objects.all().count(), 1)


