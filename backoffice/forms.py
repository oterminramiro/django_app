from django import forms
from orders_api.models import Organization, Store, Status, Item

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
		fields = ['organization', 'status' , 'name', 'address']

class ItemForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ItemForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Item
		fields = "__all__"
