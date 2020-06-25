from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as login_django , logout
from django.contrib import messages

from .forms import UserRegisterForm
# Create your views here.


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, 'Account created for ' + username)
			return redirect('login')
		else:
			context = {'form': form}
			return render(request, 'users/register.html', context)
	else:
		form = UserRegisterForm()
		context = {'form': form}
		return render(request, 'users/register.html', context)




def login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login_django(request, user)
			return redirect('main')

	context = {}
	return render(request, 'users/login.html', context)
