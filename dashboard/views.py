from django.shortcuts import render, redirect
from orders_api.models import Store
from utils.views import is_auth
# Create your views here.
def main(request):
	if not (is_auth(request)): return redirect('/users/login')

	store_count = Store.objects.count()

	context = {'store_count': store_count}

	return render(request, 'dashboard/index_content.html', context)
