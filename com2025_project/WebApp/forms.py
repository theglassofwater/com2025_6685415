from django import forms
from .models import courses


class course_selection(forms.Select):
	def create_option(self,name,value,label,selected,index,subindex=None,attrs=None):
		option = super().create_option(name,value,label,selected,index,subindex,attrs)
		if value:
			option["attrs"]["Course"] = value.instance.name 
		return option

class register_user(forms.Form):
	fname = forms.CharField(label = "First name " , max_length = 25)
	lname = forms.CharField(label = "Last name " , max_length = 25)
	username = forms.CharField(label = "Username " , max_length = 25)
	password = forms.CharField(label = "Password " , max_length = 25)
	email = forms.EmailField(label = "Email " , max_length = 100)
	course = forms.ModelChoiceField(queryset = courses.objects.all() , label = "Course")

class login_user(forms.Form):
	username = forms.CharField(label = "Username" , max_length = 25)
	password = forms.CharField(label = "Password ", max_length = 25)
