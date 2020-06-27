from django.shortcuts import render
from orders_api.models import Status, Store, Item, Customer, Order, OrderItem

# Create your views here.
def store_index(request):
	stores = Store.objects.all()
	return render(request, 'backoffice/stores.html', {'stores': stores})

def store_update(request, store_id):
	store_id = int(store_id)
	try:
		store_sel = Store.objects.get(id = store_id)
	except store.DoesNotExist:
		return redirect('store_index')

	store_form = storeCreate(request.POST or None, instance = store_sel)
	
	if store_form.is_valid():
		store_form.save()
		return redirect('store_index')

	return render(request, 'store/upload_form.html', {'upload_form':store_form})

def store_delete(request, store_id):
	store_id = int(store_id)

	try:
		store_sel = store.objects.get(id = store_id)
	except store.DoesNotExist:
		return redirect('store_index')

	store_sel.delete()
	return redirect('store_index')
