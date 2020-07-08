from django.db import models
from django.utils import timezone

class Status(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Organization(models.Model):
	status = models.ForeignKey(Status, on_delete=models.PROTECT)
	name = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Store(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
	status = models.ForeignKey(Status, on_delete=models.PROTECT)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Item(models.Model):
	status = models.ForeignKey(Status, on_delete=models.PROTECT)
	store = models.ForeignKey(Store, on_delete=models.PROTECT)
	name = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Customer(models.Model):
	name = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	phone = models.CharField(unique=True,max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class OrderItemStatus(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.PROTECT)
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	status = models.ForeignKey(OrderItemStatus, on_delete=models.PROTECT)
	item = models.ForeignKey(Item, on_delete=models.PROTECT)
	quantity = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class CustomerCode(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	code = models.CharField(max_length=6)
