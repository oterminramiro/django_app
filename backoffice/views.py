from django.shortcuts import render, redirect
from orders_api.models import Status, Organization, Store, Item
from .forms import OrganizationForm, StoreForm, ItemForm


from utils.views import is_auth

class OrganizationCrud(object):
	def organization_show(request):
		if not (is_auth(request)): return redirect('/users/login')
		organization = Organization.objects.all()
		return render(request,"backoffice/organization/show.html",{'organizations':organization})

	def organization_add(request):
		if not (is_auth(request)): return redirect('/users/login')
		if request.method == "POST":
			form = OrganizationForm(request.POST)
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
		if not (is_auth(request)): return redirect('/users/login')
		organization = Organization.objects.get(id=id)

		if request.method == "POST":
			form = OrganizationForm(request.POST, instance = organization)
			if form.is_valid():
				form.save()
				return redirect("/backoffice/organization_show")
		else:
			form = OrganizationForm(instance = organization)

		context = {'form':form, 'organization':organization}

		return render(request,'backoffice/organization/edit.html', context)

	def organization_destroy(request, id):
		if not (is_auth(request)): return redirect('/users/login')
		organization = Organization.objects.get(id=id)
		organization.delete()
		return redirect("/backoffice/organization_show")


class StoreCrud(object):

	def store_show(request, orgid):

		if not (is_auth(request)): return redirect('/users/login')

		stores = Store.objects.filter(organization = orgid)
		return render(request,"backoffice/store/show.html",{'stores':stores, 'orgid': orgid})

	def store_add(request, orgid):

		if not (is_auth(request)): return redirect('/users/login')
		if request.method == "POST":

			# Hacer el request mutable ( permitir agregarle keys al dictionary ) para luego presetearle el org_id
			request.POST._mutable = True
			request.POST['organization'] = orgid

			form = StoreForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/backoffice/store_show/' + str(orgid) )
			else:
				pass
		else:
			form = StoreForm()
		context = {'form':form , 'orgid': orgid}
		return render(request,'backoffice/store/add.html',context)

	# form para editar
	def store_edit(request, id):

		if not (is_auth(request)): return redirect('/users/login')

		store = Store.objects.get(id=id)
		orgid = store.organization.id

		if request.method == "POST":

			# Hacer el request mutable ( permitir agregarle keys al dictionary ) para luego presetearle el org_id
			request.POST._mutable = True
			request.POST['organization'] = orgid

			form = StoreForm(request.POST, instance = store)
			if form.is_valid():
				form.save()
				return redirect("/backoffice/store_show/" + str(orgid) )
		else:
			form = StoreForm(instance = store)

		context = {'form':form, 'store':store}

		return render(request,'backoffice/store/edit.html', context)

	def store_destroy(request, id):

		if not (is_auth(request)): return redirect('/users/login')

		store = Store.objects.get(id=id)
		orgid = store.organization.id

		store.delete()
		return redirect("/backoffice/store_show/" + str(orgid) )

class ItemCrud(object):

	def item_show(request, storeid):

		if not (is_auth(request)): return redirect('/users/login')

		items = Item.objects.filter(store = storeid)
		return render(request,"backoffice/item/show.html",{'items':items , 'storeid':storeid})

	def item_add(request, storeid):

		if not (is_auth(request)): return redirect('/users/login')
		if request.method == "POST":

			# Hacer el request mutable ( permitir agregarle keys al dictionary ) para luego presetearle el org_id
			request.POST._mutable = True
			request.POST['store'] = storeid

			form = ItemForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect("/backoffice/item_show/" + str(storeid) )
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

			form = ItemForm(request.POST, instance = item)
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

		item.delete()
		return redirect("/backoffice/item_show/" + str(storeid) )
