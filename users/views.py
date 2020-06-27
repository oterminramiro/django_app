from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib import messages

from utils.views import is_auth

from .forms import UserRegisterForm
# Create your views here.


def register(request):
	if (is_auth(request)): return redirect('/users/index')
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account created for ' + username)
			return redirect('/users/login')
		else:
			context = {'form': form}
			return render(request, 'users/register.html', context)
	else:
		form = UserRegisterForm()
		context = {'form': form}
		return render(request, 'users/register.html', context)

def login(request):
	if (is_auth(request)): return redirect('/users/index')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login_django(request, user)
			return redirect('/users/index')

	context = {}
	return render(request, 'users/login.html', context)

def index(request):
	if not (is_auth(request)): return redirect('/users/login')
	return render(request,'dashboard/base_template.html')

def logout(request):
	if not (is_auth(request)): return redirect('/users/login')
	logout_django(request)
	return redirect('/users/login')
