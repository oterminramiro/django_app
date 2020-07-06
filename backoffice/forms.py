from django import forms
from orders_api.models import Store, Status, Item

class StoreForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(StoreForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Store
		fields = "__all__"

class ItemForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ItemForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Item
		fields = "__all__"
