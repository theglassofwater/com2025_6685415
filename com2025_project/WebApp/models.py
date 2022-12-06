from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,BaseUserManager


# Create your models here.

class courses(models.Model):
	name = models.CharField(max_length = 25, unique = True)
	def __str__(self):
		return self.name

class users(models.Model):
	fname = models.CharField(verbose_name= "First name",max_length = 25)
	lname = models.CharField(verbose_name= "Last name",max_length = 25)
	username = models.CharField(verbose_name= "Username",max_length = 25, unique = True)
	password = models.CharField(verbose_name= "Password",max_length = 25)
	email = models.EmailField(verbose_name= "Email ",max_length = 100)
	course = models.ForeignKey(courses, verbose_name= "Course",on_delete = models.CASCADE)
	def __str__(self):
		return self.username
	def get_password(self):
		return self.password


class modules(models.Model):
	name = models.CharField(max_length = 50, primary_key = True)
	course = models.ForeignKey(courses, on_delete = models.CASCADE)
	credits = models.IntegerField(default = 15)
	one = 1
	two = 2
	Semester_choice = ((one,"one"),(two,"two"))
	semester = models.IntegerField(default = one, choices = Semester_choice)
	def __str__(self):
		return self.name + ", " + str(self.credits)

class user_modules(models.Model):
	user = models.ForeignKey(users, on_delete = models.CASCADE)
	module = models.ForeignKey(modules, on_delete = models.CASCADE)
	def __str__(self):
		return self.name + ", " + self.module