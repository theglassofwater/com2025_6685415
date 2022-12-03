from django.db import models

# Create your models here.

class users(models.Model):

	username = models.CharField(max_length = 25)
	password = models.CharField(max_length = 25)
	email = models.EmailField(max_length = 100)





	def __str__(self):
		return self.username

