from django.shortcuts import render, redirect
# Update password
from django.contrib.auth import authenticate
from django.contrib.auth import update_session_auth_hash
# Model user
from django.contrib.auth.models import User
# Authentication functions
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
# Message for creating users
from django.contrib import messages
# Utils functions
from utils.views import is_auth
# Forms
from .forms import UserRegisterForm, UserEditForm, PasswordChangeCustomForm


class UserAuth(object):
	def register(request):
		if (is_auth(request)): return redirect('/')
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
		if (is_auth(request)): return redirect('/')
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			if user is not None:
				login_django(request, user)
				return redirect('/')

		context = {}
		return render(request, 'users/login.html', context)

	def logout(request):
		if not (is_auth(request)): return redirect('/users/login')
		logout_django(request)
		return redirect('/users/login')

class UserProfile(object):

	def edit_info(request):
		if not (is_auth(request)): return redirect('/users/login')
		user_id = request.user.id
		user = User.objects.get(id = user_id)

		if request.method == 'POST':
			form = UserEditForm(request.POST, instance = user)
			if form.is_valid():
				user = form.save()
				messages.success(request, 'Your profile was successfully updated!')
				return redirect('/users/edit_info')
			else:
				context = {'form': form}
				return render(request, 'users/edit_info.html', context)

		else:
			form = UserEditForm(instance = user)
			context = {'form': form}
			return render(request, 'users/edit_info.html', context)

	def edit_pass(request):
		if not (is_auth(request)): return redirect('/users/login')
		if request.method == 'POST':
			form = PasswordChangeCustomForm(request.user, request.POST)
			if form.is_valid():
				user = form.save()
				update_session_auth_hash(request, user)
				messages.success(request, 'Your password was successfully updated!')
				return redirect('/users/edit_pass')
			else:
				context = {'form': form}
				return render(request, 'users/edit_password.html', context)

		else:
			form = PasswordChangeCustomForm(request.user)
			context = {'form': form}
			return render(request, 'users/edit_password.html', context)

	def view_info(request):
		if not (is_auth(request)): return redirect('/users/login')
		context = {}
		return render(request, 'users/profile.html', context)
