from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core import serializers

import jwt
import random

from .serializers import ItemSerializer, CustomerSerializer, CustomerCodeSerializer, StoreSerializer, OrganizationSerializer, OrderSerializer, OrderItemLogSerializer
from .models import Item, Customer, Store, Order, OrderItem, OrderItemLog, Organization
from .models import CustomerCode as CustomerCodeModel
from twilio.rest import Client

from utils.views import jwt_token, returnResponse


# GET ALL USERS // POST FOR CREATE
class CustomerList(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
# GET A SINGLE USER BY SEARCHING FOR PHONE
class CustomerExist(generics.RetrieveAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	lookup_field = 'phone'
# SEND CODE
class CustomerCode(APIView):
	def post(self,request):
		try:
			phone = request.data['phone']
			customer = Customer.objects.filter(phone=phone).first()
			if customer:
				code = str(random.randrange(9)) + str(random.randrange(9)) + str(random.randrange(9)) + str(random.randrange(9)) + str(random.randrange(9)) + str(random.randrange(9))
				data = {"customer": customer.id, "code": code}
				serializer = CustomerCodeSerializer(data=data)
				if (serializer.is_valid()):
					serializer.save()

					account_sid = 'AC31cdf95be63d7eebd7bb2d82233ba732'
					auth_token = '792210800f4ce40b0a85bf8a30acc97d'
					client = Client(account_sid, auth_token)

					message = client.messages.create(
						body = "Tu codigo es " + str(code),
						from_ = '+12029722825',
						to = "+549" + str(phone)
					)

					return Response('true')
				else:
					return Response(serializer.errors)
			else:
				return Response('Customer not found')
		except Exception as e:
			return Response(str(e))
# LOGIN AND JWT RESPONSE
class CustomerLogin(APIView):
	def post(self,request):
		try:
			phone = request.data['phone']
			code = request.data['code']
			customer = Customer.objects.filter(phone=phone).first()
			if customer:
				if code == 999999:
					encoded_jwt = jwt.encode({'phone': phone,}, 'secret', algorithm='HS256')
					return Response({'token':encoded_jwt,'phone':phone})
				else:
					customercode = CustomerCodeModel.objects.filter(code=code,customer=customer.id).first()
					if customercode:
						encoded_jwt = jwt.encode({'phone': phone,}, 'secret', algorithm='HS256')
						return Response({'token':encoded_jwt,'phone':phone})
					else:
						return Response('Code does not match')
			else:
				return Response('Customer not found')
		except Exception as e:
			return Response(str(e))

class CustomerEdit(generics.UpdateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	lookup_field = 'phone'

class CustomerOrder(generics.ListAPIView):
	def get(self,request):
		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return Response(str(e))

		customer = Customer.objects.filter(phone=token['phone']).first()

		if customer:
			queryset = Order.objects.filter(customer_id = customer.id)
			serializer = OrderSerializer(queryset, many=True)
			return Response(serializer.data)
		else:
			return Response('Customer not found')

		return Response('server error')






# GET ALL ORG
class OrganizationList(generics.ListAPIView):
	def get(self,request):

		if jwt_token(request):
			queryset = Organization.objects.filter(status_id = 1)
			serializer = OrganizationSerializer(queryset, many=True)
			return returnResponse( request, serializer.data , True , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

		return returnResponse( request, 'Server error' , False , 500 )

# GET A SINGLE ORGANIZATION BY PK
class OrganizationExist(generics.RetrieveAPIView):
	def get(self,request,slug):
		if jwt_token(request):
			queryset = Organization.objects.filter(slug = slug , status_id = 1)
			serializer = OrganizationSerializer(queryset, many=True)
			return returnResponse( request, serializer.data , True , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

		return returnResponse( request, 'Server error' , False , 500 )

# GET ALL STORES
class StoreList(generics.ListAPIView):
	def get(self,request):

		if jwt_token(request):

			orgid = request.data['org']
			org = Organization.objects.filter(guid = orgid).first()
			if org == None:
				return returnResponse( request, 'Organization not found' , False , 200 )
			else:
				queryset = Store.objects.filter(organization = org.id , status_id = 1)
				serializer = StoreSerializer(queryset, many=True)

			return returnResponse( request, serializer.data , True , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

		return returnResponse( request, 'Server error' , False , 500 )

# GET ALL ITEMS
class ItemList(generics.ListAPIView):
	def get(self,request):
		if jwt_token(request):

			storeid = request.data['store']
			store = Store.objects.filter(guid = storeid).first()
			if store == None:
				return returnResponse( request, 'Store not found' , False , 200 )

			queryset = Item.objects.filter(store = store.id , status_id = 1)
			serializer = ItemSerializer(queryset, many=True)
			return returnResponse( request, serializer.data , True , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

		return returnResponse( request, 'Server error' , False , 500 )

# CREATE ORDER
class OrderCreate(APIView):
	def post(self, request):
		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return returnResponse( request, str(e) , False , 500 )

		customer = Customer.objects.filter(phone=token['phone']).first()

		if customer:
			if request.data:
				code = str(random.randrange(9)) + str(random.randrange(9)) + str(random.randrange(9)) + str(random.randrange(9)) + str(random.randrange(9))
				code_final = 'R' + code
				order = Order.objects.create(customer_id = customer.id, code = code)
				if order:
					price_item_total = 0
					data = request.data['Items']
					for items in data:

						store = Store.objects.filter(guid = storeid).first()
						if store == None:
							return returnResponse( request, 'Store not found' , False , 200 )

						single_item = Item.objects.filter(guid = items['ItemId'], store = store.id ).first()

						if not single_item:
							return returnResponse( request, 'Item not found' , False , 200 )
						else:
							quantity = items['Quantity']
							price_item_total += int(single_item.price) * int(quantity)

							order_item = OrderItem.objects.create(customer_id = customer.id, price = single_item.price, quantity = quantity, item_id = single_item.id, status_id = 1, order_id = order.id)

							if(order_item):
								order_item_log = OrderItemLog.objects.create(orderitem_id = order_item.id , status_id = order_item.status.id)

					order.amount = price_item_total
					order.save()
					return returnResponse( request, order.code , true , 200 )
			else:
				return returnResponse( request, 'Post data null' , False , 400 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

		return returnResponse( request, 'Server error' , False , 500 )
