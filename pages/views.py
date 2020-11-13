from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Submit
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 


def home(request, *args, **kwargs):
	return render(request, 'pages/home.html', {})


def login_page(request, *args, **kwargs):
	if request.method == 'POST':
		username 	= request.POST.get('username')
		password	= request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			return redirect('panel')

		else:
			messages.error(request, 'The username or password is incorrect!')
			return render(request, 'pages/log-in.html', {})


	return render(request, 'pages/log-in.html', {})

def logout_user(request):
	logout(request)
	return redirect('home')

def sign_up(request, *args, **kwargs):

	if request.user.is_authenticated:
		return redirect('panel')
	else:

		if request.method == 'POST':

			submit=Submit()

			email	 = request.POST.get('email')
			phone	 = request.POST.get('phone')
			name	 = request.POST.get('name')
			date 	 = request.POST.get('date')
			message = request.POST.get('message')

			submit.email	=email
			submit.phone	=phone
			submit.name		=name
			submit.date		=date
			submit.messages	=messages

			submit.save()



			print('it was ok')
			print(email)
			return redirect('home')
		#messages.success(request, f'Your information was submitted, hang on tight!')
		#return render(request, 'pages/home.html', {'name':name})

		else:
			return render(request, 'pages/sign-up.html', {})


#@login_required(login_url='login')
#def dashboard(request, *args, **kwargs):
#	return render(request, 'pages/dashboard.html', {})




def about_us(request, *args, **kwargs):
	return render(request, 'pages/about-us.html', {})

def members_page(request):
	return render(request, 'pages/members.html', {})



