from rest_framework import serializers

from .models import Status, Store, Item, Customer, Order, OrderItem, CustomerCode

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
	def validate(self, data):
		if len(str(data['phone'])) != 10 :
			raise serializers.ValidationError("phone must be valid")
		return data

	class Meta:
		model = Customer
		fields = ('name', 'lastname', 'phone', 'created', 'updated')

class OrderSerializer(serializers.ModelSerializer):
	customer = CustomerSerializer(many=False, read_only=False, required=True)

	class Meta:
		model = Order
		fields = ('customer', 'created', 'updated')

class OrderItemSerializer(serializers.ModelSerializer):
	customer = CustomerSerializer(many=False, read_only=False, required=True)
	item = ItemSerializer(many=True, read_only=False, required=True)

	class Meta:
		model = OrderItem
		fields = ('customer', 'item', 'quantity', 'price', 'created', 'updated')

class CustomerCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerCode
		fields = ('customer', 'code')
