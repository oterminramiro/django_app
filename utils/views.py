from django.shortcuts import render, redirect
from orders_api.models import Customer
import jwt

def is_auth(request):
	if request.user.is_authenticated:
		return True
	else:
		return False

def jwt_token(request):
	try:
		token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
	except Exception as e:
		return Response(str(e))

	customer = Customer.objects.filter(phone=token['phone']).first()

	if customer:
		return True
	else:
		return False
