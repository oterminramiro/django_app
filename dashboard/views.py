from django.shortcuts import render, redirect
from orders_api.models import Store, Item, Customer, Order
from utils.views import is_auth
# Create your views here.
def main(request):
	if not (is_auth(request)): return redirect('/users/login')

	store_count = Store.objects.count()
	item_count = Item.objects.count()
	customer_count = Customer.objects.count()
	order_count = Order.objects.count()

	context = {'store_count': store_count, 'item_count': item_count, 'customer_count': customer_count, 'order_count': order_count}

	return render(request, 'dashboard/index_content.html', context)
