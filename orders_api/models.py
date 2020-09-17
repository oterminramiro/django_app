from django.db import models
from django.utils import timezone
import uuid

class Status(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class PaymentMethod(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class DocumentType(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class ShippingMethod(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Organization(models.Model):
	status = models.ForeignKey(Status, on_delete=models.PROTECT)
	paymentmethod = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
	shippingmethod = models.ForeignKey(ShippingMethod, on_delete=models.PROTECT)
	name = models.CharField(max_length=100)
	slug = models.CharField(max_length=100)
	logo = models.FileField(upload_to='static/img/uploads/organization/')
	guid = models.UUIDField(default=uuid.uuid4, editable=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Store(models.Model):
	organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
	status = models.ForeignKey(Status, on_delete=models.PROTECT)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	logo = models.FileField(upload_to='static/img/uploads/store/')
	guid = models.UUIDField(default=uuid.uuid4, editable=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

class Item(models.Model):
	status = models.ForeignKey(Status, on_delete=models.PROTECT)
	store = models.ForeignKey(Store, on_delete=models.PROTECT)
	name = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	description = models.CharField(max_length=400)
	logo = models.FileField(upload_to='static/img/uploads/logo/')
	guid = models.UUIDField(default=uuid.uuid4, editable=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class Customer(models.Model):
	name = models.CharField(max_length=100, blank=True)
	lastname = models.CharField(max_length=100, blank=True)
	phone = models.CharField(unique=True,max_length=100)
	email = models.CharField(unique=True,max_length=100, blank=True)
	birthday = models.DateField(blank=True)
	documentType = models.ForeignKey(DocumentType, on_delete=models.PROTECT)
	documentNumber = models.CharField(unique=True,max_length=100, blank=True)
	idmercadopago = models.CharField(max_length=200, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class OrderItemStatus(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	amount = models.CharField(max_length=100, blank=True)
	code = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="orderitem")
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	status = models.ForeignKey(OrderItemStatus, on_delete=models.PROTECT)
	item = models.ForeignKey(Item, on_delete=models.PROTECT)
	quantity = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class OrderItemLog(models.Model):
	orderitem = models.ForeignKey(OrderItem, on_delete=models.PROTECT, related_name="orderitem")
	status = models.ForeignKey(OrderItemStatus, on_delete=models.PROTECT)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

class CustomerCode(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
	code = models.CharField(max_length=6)
