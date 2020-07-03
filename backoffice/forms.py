from django import forms
from orders_api.models import Store, Status

class StoreForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(StoreForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

	Status = forms.ModelChoiceField(queryset=Status.objects.all())

	class Meta:
		model = Store
		fields = "__all__"
