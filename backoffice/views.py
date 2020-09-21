from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from orders_api.models import Status, Organization, Store, Item, Order, OrderItem, OrderItemLog, Customer
from users.models import User, UserOrganization
from .forms import OrganizationForm, StoreForm, ItemForm, UserForm, UserEditForm, UserOrgAddForm

from utils.views import is_auth, check_role, check_role_and_auth

class OrganizationCrud(object):

	def organization_show(request):


		check_role_and_auth(request,['ADMIN'])
		organization = Organization.objects.all().order_by('id')
		return render(request,"backoffice/organization/show.html",{'organizations':organization})

	def organization_add(request):
		check_role_and_auth(request,['ADMIN'])
		if request.method == "POST":
			form = OrganizationForm(request.POST, request.FILES)
			if form.is_valid():
				try:
					form.save()
					return redirect('/backoffice/organization_show')
				except:
					pass
		else:
			form = OrganizationForm()

		return render(request,'backoffice/organization/add.html',{'form':form})

	def organization_edit(request, id):
		check_role_and_auth(request,['ADMIN'])
		organization = Organization.objects.get(id=id)

		if request.method == "POST":
			form = OrganizationForm(request.POST, request.FILES, instance = organization)
			if form.is_valid():
				form.save()
				return redirect("/backoffice/organization_show")
		else:
			form = OrganizationForm(instance = organization)

		context = {'form':form, 'organization':organization}

		return render(request,'backoffice/organization/edit.html', context)

	def organization_destroy(request, id):
		check_role_and_auth(request,['ADMIN'])
		organization = Organization.objects.get(id=id)
		try:
			delete = organization.delete()
			return HttpResponse(True)
		except Exception as e:
			return HttpResponse(False)

class StoreCrud(object):

	def store_show(request, orgid = None):
		check_role_and_auth(request,['ADMIN','OWNER'])
		if(orgid != None):
			stores = Store.objects.filter(organization = orgid).order_by('id')
		else:
			stores = Store.objects.all().order_by('id')
		return render(request,"backoffice/store/show.html",{'stores':stores, 'orgid': orgid})

	def store_add(request, orgid = None):

		check_role_and_auth(request,['ADMIN','OWNER'])
		if request.method == "POST":

			if(orgid != None):
				# Hacer el request mutable ( permitir agregarle keys al dictionary ) para luego presetearle el org_id
				request.POST._mutable = True
				request.POST['organization'] = orgid

			form = StoreForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				if(orgid != None):
					return redirect('/backoffice/store_show/' + str(orgid) )
				else:
					return redirect('/backoffice/store_show')
			else:
				pass
		else:
			form = StoreForm()
		context = {'form':form , 'orgid': orgid}
		return render(request,'backoffice/store/add.html',context)

	def store_edit(request, id):

		check_role_and_auth(request,['ADMIN','OWNER'])
		store = Store.objects.get(id=id)
		orgid = store.organization.id

		if request.method == "POST":

			# Hacer el request mutable ( permitir agregarle keys al dictionary ) para luego presetearle el org_id
			request.POST._mutable = True
			request.POST['organization'] = orgid

			form = StoreForm(request.POST, request.FILES, instance = store)
			if form.is_valid():
				form.save()
				return redirect('/backoffice/store_show')
		else:
			form = StoreForm(instance = store)

		context = {'form':form, 'store':store}

		return render(request,'backoffice/store/edit.html', context)

	def store_destroy(request, id):

		check_role_and_auth(request,['ADMIN','OWNER'])
		store = Store.objects.get(id=id)
		orgid = store.organization.id

		try:
			delete = store.delete()
			return HttpResponse(True)
		except Exception as e:
			return HttpResponse(False)

class ItemCrud(object):

	def item_show(request, storeid = None):

		if not (is_auth(request)): return redirect('/users/login')
		if(storeid != None):
			# get orgid for return button
			store = Store.objects.filter(id = storeid)[0]
			items = Item.objects.filter(store = storeid).order_by('id')
			return render(request,"backoffice/item/show.html",{'items':items , 'storeid':storeid, 'orgid':store.organization.id})
		else:
			items = Item.objects.all().order_by('id')
			return render(request,"backoffice/item/show.html",{'items':items , 'storeid':storeid})

	def item_add(request, storeid = None):

		if not (is_auth(request)): return redirect('/users/login')
		if request.method == "POST":

			if(storeid != None):
				# Hacer el request mutable ( permitir agregarle keys al dictionary ) para luego presetearle el org_id
				request.POST._mutable = True
				request.POST['store'] = storeid

			form = ItemForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				if(storeid != None):
					return redirect("/backoffice/item_show/" + str(storeid) )
				else:
					return redirect("/backoffice/item_show" )
			else:
				pass
		else:
			form = ItemForm()
		context = {'form': form , 'storeid': storeid}
		return render(request,'backoffice/item/add.html',context)

	def item_edit(request, id):
		if not (is_auth(request)): return redirect('/users/login')

		item = Item.objects.get(id=id)
		storeid = item.store.id

		if request.method == "POST":

			# Hacer el request mutable ( permitir agregarle keys al dictionary ) para luego presetearle el org_id
			request.POST._mutable = True
			request.POST['store'] = storeid

			form = ItemForm(request.POST, request.FILES, instance = item)
			if form.is_valid():
				form.save()
				return redirect("/backoffice/item_show/" + str(storeid) )
		else:
			form = ItemForm(instance = item)

		context = {'form':form, 'item':item}

		return render(request,'backoffice/item/edit.html', context)

	def item_destroy(request, id):
		if not (is_auth(request)): return redirect('/users/login')

		item = Item.objects.get(id=id)
		storeid = item.store.id

		try:
			delete = item.delete()
			return HttpResponse(True)
		except Exception as e:
			return HttpResponse(False)

class OrderCrud(object):
	def order_show(request):
		if not (is_auth(request)): return redirect('/users/login')

		orders = Order.objects.prefetch_related('orderitem').all()

		response = []
		for order in orders:

			id = order.id
			created = order.created
			fullname  = order.customer.name + ' ' + order.customer.lastname

			orderitems = order.orderitem.all()
			total = 0
			array_item_names = []
			array_status = []

			for orderitem in orderitems:
				total += int(orderitem.price) * int(orderitem.quantity)
				array_item_names.append(orderitem.item.name)
				array_status.append(orderitem.status.name)

			dict = {
				"id": id,
				"created": created,
				"fullname": fullname,
				"status": list(set(array_status)),
				"item_names": list(set(array_item_names)),
				"total": total
			}
			response.append(dict)

		return render(request,"backoffice/order/show.html",{'orders':response})

	def order_log(request, orderid):

		if not (is_auth(request)): return redirect('/users/login')

		response = [];
		order_item = OrderItem.objects.filter(order_id = orderid)
		for orderitem in order_item:
			orderitemlog = OrderItemLog.objects.filter(orderitem_id = orderitem.id)
			response.append(orderitemlog)

		return render(request,"backoffice/order/log.html",{'logs':response})

class UserCrud(object):

	def owner_show(request):
		if not (is_auth(request)): return redirect('/users/login')
		users = User.objects.filter(role=2)
		return render(request,"backoffice/user/owner_show.html",{'users':users})

	def owner_add(request):

		if not (is_auth(request)): return redirect('/users/login')
		if request.method == "POST":

			request.POST._mutable = True
			request.POST['role'] = 2

			form = UserForm(request.POST)
			if form.is_valid():
				# Hash password and save
				user = form.save(commit=False)
				password = form.cleaned_data['password']
				user.set_password(password)
				user.save()
				return redirect("/backoffice/owner_show" )
			else:
				pass
		else:
			form = UserForm()
		context = {'form': form}
		return render(request,'backoffice/user/owner_add.html',context)

	def seller_show(request):
		if not (is_auth(request)): return redirect('/users/login')
		users = User.objects.filter(role=3)
		return render(request,"backoffice/user/seller_show.html",{'users':users})

	def seller_add(request):

		if not (is_auth(request)): return redirect('/users/login')
		if request.method == "POST":

			request.POST._mutable = True
			request.POST['role'] = 3

			form = UserForm(request.POST)
			if form.is_valid():
				# Hash password and save
				user = form.save(commit=False)
				password = form.cleaned_data['password']
				user.set_password(password)
				user.save()
				return redirect("/backoffice/seller_show" )
			else:
				pass
		else:
			form = UserForm()
		context = {'form': form}
		return render(request,'backoffice/user/seller_add.html',context)

	def user_edit(request, id):
		if not (is_auth(request)): return redirect('/users/login')

		user = User.objects.get(id=id)

		if request.method == "POST":

			form = UserEditForm(request.POST, instance = user)
			if form.is_valid():
				form.save()
				if user.role_id == 2:
					return redirect("/backoffice/owner_show" )
				if user.role_id == 3:
					return redirect("/backoffice/seller_show" )
		else:
			form = UserEditForm(instance = user)

		context = {'form':form, 'user':user}

		return render(request,'backoffice/user/edit.html', context)

	def user_destroy(request, id):
		if not (is_auth(request)): return redirect('/users/login')

		user = User.objects.get(id=id)
		try:
			delete = user.delete()
			return HttpResponse(True)
		except Exception as e:
			return HttpResponse(False)


	def user_org_show(request, userid):
		if not (is_auth(request)): return redirect('/users/login')

		user = User.objects.get(id=userid)
		colection = UserOrganization.objects.filter(user_id = user.id)

		response = []
		for user_org in colection:
			dict = { 'id': user_org.id , 'name': user_org.organization.name }
			response.append(dict)

		context = {'org':response , 'userid': userid }
		return render(request,"backoffice/user/user_org_show.html",context)

	def user_org_add(request, userid):
		if not (is_auth(request)): return redirect('/users/login')
		if request.method == "POST":

			request.POST._mutable = True
			request.POST['user'] = userid

			form = UserOrgAddForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect("/backoffice/user_org_show/" + str(userid) )
			else:
				pass
		else:
			form = UserOrgAddForm()
		context = {'form': form , 'userid': userid}
		return render(request,'backoffice/user/user_org_add.html',context)

	def user_org_destroy(request, id):
		if not (is_auth(request)): return redirect('/users/login')

		user_org = UserOrganization.objects.get(id=id)
		userid = user_org.user_id
		user_org.delete()

		return redirect("/backoffice/user_org_show/" + str(userid) )

class CustomerCrud(object):
	def customer_show(request):
		if not (is_auth(request)): return redirect('/users/login')
		customers = Customer.objects.all()
		return render(request,"backoffice/customer/show.html",{'customers':customers})

	def customer_destroy(request, id):
		if not (is_auth(request)): return redirect('/users/login')

		customer = Customer.objects.get(id=id)
		try:
			delete = customer.delete()
			return HttpResponse(True)
		except Exception as e:
			return HttpResponse(False)
