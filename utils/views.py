from django.shortcuts import render, redirect

def is_auth(request):
	if request.user.is_authenticated:
		return True
	else:
		return False
