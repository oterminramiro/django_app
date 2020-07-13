from rest_framework import serializers

from .models import Status,PaymentMethod, ShippingMethod, Organization, Store, Item, Customer, Order, OrderItemStatus, OrderItem, OrderItemLog, CustomerCode

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = ('name', 'key')

class PaymentMethodSerializer(serializers.ModelSerializer):
	class Meta:
		model = PaymentMethod
		fields = ('name', 'key')

class ShippingMethodSerializer(serializers.ModelSerializer):
	class Meta:
		model = ShippingMethod
		fields = ('name', 'key')

class OrganizationSerializer(serializers.ModelSerializer):
	status = serializers.StringRelatedField(many=False)
	paymentmethod = serializers.StringRelatedField(many=False)
	shippingmethod = serializers.StringRelatedField(many=False)

	class Meta:
		model = Organization
		fields = ('status', 'name', 'slug', 'created', 'updated')

class StoreSerializer(serializers.ModelSerializer):
	organization =serializers.StringRelatedField(many=False)
	status = serializers.StringRelatedField(many=False)

	class Meta:
		model = Store
		fields = ('organization', 'status', 'name', 'address', 'created', 'updated')

class ItemSerializer(serializers.ModelSerializer):
	store = serializers.StringRelatedField(many=False)
	status = serializers.StringRelatedField(many=False)

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
		fields = ('name', 'lastname', 'phone', 'email', 'birthday', 'created', 'updated')

class OrderItemStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = OrderItemStatus
		fields = ('name', 'key')

class OrderItemSerializer(serializers.ModelSerializer):
	orderid = serializers.StringRelatedField(many=False)
	orderitemstatus = serializers.StringRelatedField(many=False)
	item = ItemSerializer(many=False, read_only=False, required=True)

	class Meta:
		model = OrderItem
		fields = ('orderitemstatus','orderid', 'item', 'quantity', 'price', 'created', 'updated')

class OrderSerializer(serializers.ModelSerializer):
	customer = CustomerSerializer(many=False, read_only=False, required=True)
	orderitem = OrderItemSerializer(many=True, read_only=True)
	class Meta:
		model = Order
		fields = ('customer', 'created', 'updated', 'orderitem')

class OrderItemLogSerializer(serializers.ModelSerializer):
	orderitem = OrderItemSerializer(many=False)
	orderitemstatus = serializers.StringRelatedField(many=False)

	class Meta:
		model = OrderItemLog
		fields = ('orderitem', 'orderitemstatus', 'created', 'updated')


class CustomerCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerCode
		fields = ('customer', 'code')
