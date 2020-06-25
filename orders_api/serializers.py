from rest_framework import serializers

from .models import Status, Store, Item, Customer, Order, OrderItem

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('name', 'key')

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('status', 'name', 'address', 'created', 'updated')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('status', 'store', 'name', 'price', 'created', 'updated')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'lastname', 'phone', 'created', 'updated')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('customer', 'created', 'updated')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('customer', 'item', 'quantity', 'price', 'created', 'updated')
