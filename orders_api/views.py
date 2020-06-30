from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.core import serializers

import jwt
import random

from .serializers import ItemSerializer, CustomerSerializer, CustomerCodeSerializer
from .models import Item, Customer
from .models import CustomerCode as CustomerCodeModel

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

# GET ALL ITEMS
class ItemList(generics.ListAPIView):
	def get(self,request):

		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return Response(str(e))
			
		customer = Customer.objects.filter(phone=token['phone']).first()

		if customer:
			queryset = Item.objects.all()
			serializer = ItemSerializer(queryset, many=True)
			return Response(serializer.data)
		else:
			return Response('Customer not found')

		return Response('server error')
# GET A SINGLE ITEM BY PK
class ItemExist(generics.RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
