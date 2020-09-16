from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

from utils.views import returnResponse

class CreateCustomer(APIView):
	def post(self,request):
		url = "https://api.mercadopago.com/v1/customers?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"

		payload = request.data
		headers = {
			'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

		return Response( json.loads( response.text ) )

class FindCustomer(APIView):
	def post(self,request):
		url = "https://api.mercadopago.com/v1/customers/search?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"

		email = request.POST.get('email', '')
		payload = {'email': email}
		headers = {
			'accept': 'application/json',
			'Content-Type': 'application/x-www-form-urlencoded'
		}

		response = requests.request("GET", url, headers=headers, data = payload)

		result = json.loads( response.text ).get('results')[0]
		dataResponse = {
			'email' : result.get('email'),
			'first_name' : result.get('first_name'),
			'last_name' : result.get('last_name'),
			'id' : result.get('id'),
			'identification' : result.get('identification')
		}

		return returnResponse( request, dataResponse , True , 200 )

class ListCard(APIView):
	def post(self,request):

		url = "https://api.mercadopago.com/v1/customers/search?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"

		email = request.POST.get('email', '')
		payload = {'email': email}
		headers = {
			'accept': 'application/json',
			'Content-Type': 'application/x-www-form-urlencoded'
		}
		response = requests.request("GET", url, headers=headers, data = payload)
		customer_id = json.loads( response.text ).get('results')[0].get('id')

		url = "https://api.mercadopago.com/v1/customers/" + customer_id + "/cards?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"

		payload = {}
		headers= {}

		response = requests.request("GET", url, headers=headers, data = payload)

		return returnResponse( request, json.loads( response.text ) , True , 200 )

class SaveCard(APIView):
	def post(self,request):

		token = request.POST.get('token', '')

		url = "https://api.mercadopago.com/v1/customers/523839858-5OxYrmPaNezikV/cards?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"

		payload = {'token': token}
		headers = {
			'Content-Type': 'application/json'
		}

		response = requests.request("GET", url, headers=headers, data = json.dumps(payload))

		return Response( json.loads( response.text ) )

class SaveCardView(object):
	def save_card_view(request):
		return render(request,"mercadopago/addcard.html")

class Payment(APIView):
	def post(self,request):
		url = "https://api.mercadopago.com/v1/payments?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"
		token = request.POST.get('token', '')
		payload = {
			"token":token,
			"installments":1,
			"transaction_amount":50,
			"description":"Django api",
			"payment_method_id":"visa",
			"payer":{
				"email":"ramiro@cubiq.digital",
				"identification": {
		            "number": "42395005",
		            "type": "DNI"
		        }
			},
			"binary_mode": True,
			"external_reference":"DJANGO",
			"statement_descriptor":"Django"
		}
		headers = {
			'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

		return returnResponse( request, json.loads( response.text ) , True , 200 )

class PaymentView(object):
	def payment_view(request):
		return render(request,"mercadopago/payment.html")
