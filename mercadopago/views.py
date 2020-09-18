from django.shortcuts import render
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.views import returnResponse, jwt_token
import requests, json, jwt
from orders_api.models import Customer, DocumentType, Order
from django.conf import settings

class CreateCustomer(APIView):
	def post(self,request):
		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return returnResponse( request, str(e) , False , 500 )

		customer = Customer.objects.filter(phone=token['phone']).first()
		if customer:
			if customer.idmercadopago == None:
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
				if response.status_code == 200:

					mp_id = json.loads( response.text ).get("id")

					customer.idmercadopago = mp_id
					customer.save()

					return returnResponse( request, json.loads( response.text ) , True , 200 )
				else:
					return returnResponse( request, json.loads( response.text ).get('cause')[0].get('description') , False , response.status_code )
			else:
				return returnResponse( request, 'Customer is already register in mercadopago' , False , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

class FindCustomer(APIView):
	def post(self,request):
		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return returnResponse( request, str(e) , False , 500 )

		customer = Customer.objects.filter(phone=token['phone']).first()
		if customer:
			if customer.email != None:
				url = "https://api.mercadopago.com/v1/customers/search?access_token=" + settings.MP_ACCESS_TOKEN

				payload = {'email': customer.email}
				headers = {
					'accept': 'application/json',
					'Content-Type': 'application/x-www-form-urlencoded'
				}

				response = requests.request("GET", url, headers=headers, data = payload)

				if response.status_code == 200:

					result = json.loads( response.text ).get('results')[0]
					dataResponse = {
						'email' : result.get('email'),
						'first_name' : result.get('first_name'),
						'last_name' : result.get('last_name'),
						'id' : result.get('id'),
						'identification' : result.get('identification')
					}

					return returnResponse( request, dataResponse , True , 200 )

				else:
					return returnResponse( request, json.loads( response.text ).get('cause')[0].get('description') , False , response.status_code )

			else:
				return returnResponse( request, 'Customer email is none' , False , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

class ListCard(APIView):
	def post(self,request):
		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return returnResponse( request, str(e) , False , 500 )

		customer = Customer.objects.filter(phone=token['phone']).first()
		if customer:
			if customer.email != None:
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
				if response.status_code == 200:
					return returnResponse( request, json.loads( response.text ) , True , 200 )
				else:
					return returnResponse( request, json.loads( response.text ) , False , response.status_code )
			else:
				return returnResponse( request, 'Customer email is none' , False , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

class SaveCard(APIView):
	def post(self,request):
		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return returnResponse( request, str(e) , False , 500 )

		customer = Customer.objects.filter(phone=token['phone']).first()
		if customer:
			if customer.idmercadopago != None:
				token = request.POST.get('token', '')

				url = "https://api.mercadopago.com/v1/customers/" + customer.idmercadopago +"/cards?access_token=" + settings.MP_ACCESS_TOKEN

				payload = {'token': token}
				headers = {
					'Content-Type': 'application/json'
				}

				response = requests.request("GET", url, headers=headers, data = json.dumps(payload))

				if response.status_code == 200:
					return returnResponse( request, json.loads( response.text ) , True , 200 )
				else:
					return returnResponse( request, json.loads( response.text ) , False , response.status_code )
			else:
				return returnResponse( request, 'Customer idmercadopago is none' , False , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

class DeleteCard(APIView):
	def post(self,request):
		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return returnResponse( request, str(e) , False , 500 )

		customer = Customer.objects.filter(phone=token['phone']).first()
		if customer:
			if customer.idmercadopago != None:
				token = request.POST.get('token', '')
				cardid = request.POST.get('cadid', '')

				url = "https://api.mercadopago.com/v1/customers/" + customer.idmercadopago +"/cards/"+ cardid + "?access_token=" + settings.MP_ACCESS_TOKEN

				payload = {'token': token}
				headers = {
					'Content-Type': 'application/json'
				}

				response = requests.request("DELETE", url, headers=headers, data = json.dumps(payload))

				if response.status_code == 200:
					return returnResponse( request, json.loads( response.text ) , True , 200 )
				else:
					return returnResponse( request, json.loads( response.text ) , False , response.status_code )
			else:
				return returnResponse( request, 'Customer idmercadopago is none' , False , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )

class SaveCardView(object):
	def save_card_view(request):
		return render(request,"mercadopago/addcard.html")

class Payment(APIView):
	def post(self,request):
		try:
			token = jwt.decode(request.headers['x-auth-token'], 'secret', algorithms=['HS256'])
		except Exception as e:
			return returnResponse( request, str(e) , False , 500 )

		customer = Customer.objects.filter(phone=token['phone']).first()
		if customer:
			if customer.email != None:
				url = "https://api.mercadopago.com/v1/payments?access_token=" + settings.MP_ACCESS_TOKEN

				token = request.POST.get('token', '')
				idorder = request.POST.get('idorder', '')

				order = Order.objects.filter(id=idorder).first()
				if order == None:
					return returnResponse( request, 'Order not found' , False , 404 )

				documentType = DocumentType.objects.filter(id=customer.documentType_id).first()

				payload = {
					"token": token,
					"installments": 1,
					"transaction_amount": order.amount,
					"description": "Django api",
					"payer":{
						"email": customer.email,
						"identification": {
							"number": customer.documentNumber,
							"type": documentType.key if documentType != None else None,
						}
					},
					"binary_mode": True,
					"external_reference": "DJANGO",
					"statement_descriptor": "Django"
				}
				headers = {
					'Content-Type': 'application/json'
				}

				response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

				if response.status_code == 200:
					return returnResponse( request, json.loads( response.text ) , True , 200 )
				else:
					return returnResponse( request, json.loads( response.text ) , False , response.status_code )
			else:
				return returnResponse( request, 'Customer email is none' , False , 200 )
		else:
			return returnResponse( request, 'Customer not found' , False , 200 )


class PaymentView(object):
	def payment_view(request):
		return render(request,"mercadopago/payment.html")
