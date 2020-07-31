from django import forms
from orders_api.models import Organization, Store, Status, Item
from users.models import User, UserOrganization

class OrganizationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(OrganizationForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Organization
		fields = "__all__"

class StoreForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(StoreForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Store
		fields = ['organization', 'status' , 'name', 'address', 'logo']

class ItemForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ItemForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Item
		fields = "__all__"

class UserForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = User
		fields = ['role', 'username','email','first_name','last_name','password']

class UserEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserEditForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = User
		fields = ['username','email','first_name','last_name']

class UserOrgAddForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(UserOrgAddForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = UserOrganization
		fields = ['user','organization']
