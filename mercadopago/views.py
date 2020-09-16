from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.views import returnResponse, jwt_token
import requests, json, jwt
from orders_api.models import Customer, DocumentType
from django.conf import settings

class CreateCustomer(APIView):
	def post(self,request):
		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return returnResponse( request, str(e) , False , 500 )

		customer = Customer.objects.filter(phone=token['phone']).first()
		if customer:
			url = "https://api.mercadopago.com/v1/customers?access_token=" + settings.MP_ACCESS_TOKEN
			documentType = DocumentType.objects.filter(id=customer.documentType_id).first()

			payload = {
				"email": customer.email,
				"first_name": customer.name,
				"last_name": customer.lastname,
				"identification": {
					"type": documentType.key if documentType != None else None,
					"number": customer.documentNumber
				}
			}
			headers = {
				'Content-Type': 'application/json'
			}

			response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

			mp_id = json.loads( response.text ).get("id")

			customer.idmercadopago = mp_id
			customer.save()

			return returnResponse( request, json.loads( response.text ) , True , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )


class FindCustomer(APIView):
	def post(self,request):
		url = "https://api.mercadopago.com/v1/customers/search?access_token=" + settings.MP_ACCESS_TOKEN

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

		url = "https://api.mercadopago.com/v1/customers/search?access_token=" + settings.MP_ACCESS_TOKEN

		email = request.POST.get('email', '')
		payload = {'email': email}
		headers = {
			'accept': 'application/json',
			'Content-Type': 'application/x-www-form-urlencoded'
		}
		response = requests.request("GET", url, headers=headers, data = payload)
		customer_id = json.loads( response.text ).get('results')[0].get('id')

		url = "https://api.mercadopago.com/v1/customers/" + customer_id + "/cards?access_token=" + settings.MP_ACCESS_TOKEN

		payload = {}
		headers= {}

		response = requests.request("GET", url, headers=headers, data = payload)

		return returnResponse( request, json.loads( response.text ) , True , 200 )

class SaveCard(APIView):
	def post(self,request):

		token = request.POST.get('token', '')

		url = "https://api.mercadopago.com/v1/customers/523839858-5OxYrmPaNezikV/cards?access_token=" + settings.MP_ACCESS_TOKEN

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
		url = "https://api.mercadopago.com/v1/payments?access_token=" + settings.MP_ACCESS_TOKEN
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
