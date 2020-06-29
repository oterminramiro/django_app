from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import StatusSerializer, StoreSerializer, ItemSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer
from .models import Status, Store, Item, Customer, Order, OrderItem

# GET ALL USERS // POST FOR CREATE
class CustomerList(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
# GET A SINGLE USER BY SEARCHING FOR PHONE
class CustomerExist(generics.RetrieveAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer
	lookup_field = 'phone'


# GET ALL ITEMS
class ItemList(generics.ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
# GET A SINGLE ITEM BY PK
class ItemExist(generics.RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
