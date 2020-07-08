from rest_framework import serializers

from .models import Status, Organization, Store, Item, Customer, Order, OrderItemStatus, OrderItem, CustomerCode

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ('name', 'key')

class OrganizationSerializer(serializers.ModelSerializer):
	status = serializers.StringRelatedField(many=False)

	class Meta:
		model = Organization
		fields = ('status', 'name', 'created', 'updated')

class StoreSerializer(serializers.ModelSerializer):
	organization =serializers.StringRelatedField(many=True)
	status = serializers.StringRelatedField(many=True)

	class Meta:
		model = Store
		fields = ('organization', 'status', 'name', 'address', 'created', 'updated')

class ItemSerializer(serializers.ModelSerializer):
	store = serializers.StringRelatedField(many=True)
	status = serializers.StringRelatedField(many=True)

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

class OrderItemStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItemStatus
		fields = ('name', 'key')

class OrderSerializer(serializers.ModelSerializer):
	customer = serializers.StringRelatedField(many=True)

	class Meta:
		model = Order
		fields = ('customer', 'created', 'updated')

class OrderItemSerializer(serializers.ModelSerializer):
	customer = serializers.StringRelatedField(many=True)
	orderitemstatus = serializers.StringRelatedField(many=True)
	item = serializers.StringRelatedField(many=True)

	class Meta:
		model = OrderItem
		fields = ('customer', 'status', 'item', 'quantity', 'price', 'created', 'updated')

class CustomerCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerCode
		fields = ('customer', 'code')
