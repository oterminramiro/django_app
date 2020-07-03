from django.shortcuts import render, redirect
from orders_api.models import Status, Store, Item, Customer, Order, OrderItem
from .forms import StoreForm

class StoreCrud(object):

	def store_add(request):
		if request.method == "POST":
			form = StoreForm(request.POST)
			if form.is_valid():
				try:
					form.save()
					return redirect('/backoffice/store_show')
				except:
					pass
		else:
			form = StoreForm()

		return render(request,'backoffice/store/add.html',{'form':form})

	def store_show(request):
		stores = Store.objects.all()
		return render(request,"backoffice/store/show.html",{'stores':stores})

	# form para editar
	def store_edit(request, id):
		store = Store.objects.get(id=id)
		return render(request,'backoffice/store/edit.html', {'store':store})

	# procesado de datos
	def store_update(request, id):
		if request.method == "POST":
			store = Store.objects.get(id=id)
			form = StoreForm(request.POST, instance = store)
			if form.is_valid():
				form.save()
				return redirect("/backoffice/store_show")
			else:
				context = {'store': store, 'form':form}
				return render(request, 'backoffice/store/edit.html', context)

	def store_destroy(request, id):
		store = Store.objects.get(id=id)
		store.delete()
		return redirect("/backoffice/store_show")
