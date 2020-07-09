from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm

from .models import User
#from django.contrib.auth.models import User

from django import forms

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class UserEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserEditForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = User
		fields = ['username','email','first_name','last_name']

class PasswordChangeCustomForm(PasswordChangeForm):
	def __init__(self, *args, **kwargs):
		super(PasswordChangeCustomForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
