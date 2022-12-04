from django.db import models

# Create your models here.

class courses(models.Model):
	name = models.CharField(max_length = 25)
	def __str__(self):
		return self.name

class users(models.Model):
	fname = models.CharField(max_length = 25)
	lname = models.CharField(max_length = 25)
	username = models.CharField(max_length = 25)
	password = models.CharField(max_length = 25)
	email = models.EmailField(max_length = 100)
	course = models.ForeignKey(courses, on_delete = models.CASCADE)
	def __str__(self):
		return self.username

class modules(models.Model):
	name = models.CharField(max_length = 50, primary_key = True)
	course = models.ForeignKey(courses, on_delete = models.CASCADE)
	one = 1
	two = 2
	Semester_choice = ((one,"one"),(two,"two"))
	semester = models.IntegerField(default = one, choices = Semester_choice)
	def __str__(self):
		return self.name

class user_modules(models.Model):
	user = models.ForeignKey(users, on_delete = models.CASCADE)
	module = models.ForeignKey(modules, on_delete = models.CASCADE)
	def __str__(self):
		return self.name + ", " + self.module