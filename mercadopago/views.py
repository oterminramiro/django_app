from django.shortcuts import render
from rest_framework.views import APIView
import requests

class CreateCustomer(APIView):
	def post(self,request):
		url = "https://api.mercadopago.com/v1/customers?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"

		payload = {
			"email": "ramiro@cubiq.digital",
			"first_name": "Ramiro",
			"last_name": "Otermin",
			"identification": {
				"type": "DNI",
				"number": "42395005"
			}
		}

		headers = {
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data = json.dumps(payload))

		print(response.text.encode('utf8'))

class FindCustomer(APIView):
	def get(self,request):
		url = "https://api.mercadopago.com/v1/customers/search?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"

		payload = 'email=ramiro@cubiq.digital'
		headers = {
			'accept': 'application/json',
			'Content-Type': 'application/x-www-form-urlencoded'
		}

		response = requests.request("GET", url, headers=headers, data = payload)

		print(response.text.encode('utf8'))

class ListCard(APIView):
	def get(self,request):

		url = "https://api.mercadopago.com/v1/customers/523839858-5OxYrmPaNezikV/cards?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"

		payload = {}
		headers= {}

		response = requests.request("GET", url, headers=headers, data = payload)

		print(response.text.encode('utf8'))

class SaveCard(APIView):
	def post(self,request):

		token = request.POST.get('token', '')

		url = "https://api.mercadopago.com/v1/customers/523839858-5OxYrmPaNezikV/cards?access_token=TEST-6220461586437789-121822-16fb0610d868f7102a31a386c3d4c56e-358482134"

		payload = {'token': token}
		headers= {}

		response = requests.request("GET", url, headers=headers, data = json.dumps(payload))

		print(response.text.encode('utf8'))

class SaveCardView(object):
	def save_card_view(request):
		return render(request,"mercadopago/addcard.html")
