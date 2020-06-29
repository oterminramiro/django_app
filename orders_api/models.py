from django.db import models
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)

class Store(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    item = models.ForeignKey(Item, on_delete=models.PROTECT)
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
