from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from .serializers import StatusSerializer, StoreSerializer, ItemSerializer, CustomerSerializer, OrderSerializer, OrderItemSerializer
from .models import Status, Store, Item, Customer, Order, OrderItem


# class ItemViewSet(viewsets.ViewSet):
    # def list(self, request):
        # queryset = Item.objects.all()
        # serializer = ItemSerializer(queryset, many=True)
        # return Response(serializer.data)

#
    # def retrieve(self, request, pk=None):
        # queryset = User.objects.all()
        # user = get_object_or_404(queryset, pk=pk)
        # serializer = UserSerializer(user)

class StoreViewSet(viewsets.ViewSet):
	def list(self,request):
		queryset = Store.objects.all()
		serializer = StoreSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = Store.objects.all()
		item = get_object_or_404(queryset, pk=pk)
		serializer = StoreSerializer(item)
		return Response(serializer.data)

class ItemViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Item.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

class CustomerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Customer.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Customer.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CustomerSerializer(item)
        return Response(serializer.data)
