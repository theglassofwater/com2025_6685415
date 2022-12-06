from django import forms
from .models import courses,modules


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

class ContactForm(forms.Form):
	name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'formfield'}))
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'formfield'}))
	subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'formfield'}))
    
	message = forms.CharField(widget=forms.Textarea(attrs={'class': 'formfield'}), required=True)

class modules_form(forms.Form):
	# def __init__(self,site_id,*args,**kwargs):
	# 	self._pwd = kwargs.pop('pwd', None)
	# 	super().__init__(*args, **kwargs)
	# def get_course(self):
	# 	return self._pwd

	# course_name = forms.CharField()
	module1 = forms.ModelChoiceField(queryset = modules.objects.all() , label = "modules", required=True) 
	module2 = forms.ModelChoiceField(queryset = modules.objects.all() , label = "modules", required=True) 
	module3 = forms.ModelChoiceField(queryset = modules.objects.all() , label = "modules", required=True) 
	module4 = forms.ModelChoiceField(queryset = modules.objects.all() , label = "modules", required=False) 
	module5 = forms.ModelChoiceField(queryset = modules.objects.all() , label = "modules", required=False) 
