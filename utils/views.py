from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import status
from orders_api.models import Customer
from django.http import Http404
import jwt
import json

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

def check_role(request,roles):
	for role in roles:
		if role == request.user.role.name:
			return True

	#return False
	raise Http404("Not allowed")

def check_role_and_auth(request,roles):
	if request.user.is_authenticated:
		for role in roles:
			if role == request.user.role.name:
				return True

		#return False
		raise Http404("Not allowed")
	else:
		 return redirect('/users/login')

def returnResponse(request, data, status, code):
	response = {
		'success': status,
		'data': data,
	}
	return Response( response , status = code )
