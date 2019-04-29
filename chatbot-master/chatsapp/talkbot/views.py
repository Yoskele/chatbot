from django.shortcuts import render, redirect
from .forms import Loginform
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def homepage(request):
	return render(request, 'index.html')


def loginview(request):
	form = Loginform(request.POST or None)

	context =  {"from":form}


	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')

		user = authenticate(username=username, password=password)
		
		if user is None:
			messages.info(request,"Username or password is wrong")
			return render(request, "login.html",context)

		messages.succes(request,"you have made a successful entry")	
		login(request,user)
		return redirect('homepage')


	return render(request, 'login.html', {'form': form})

