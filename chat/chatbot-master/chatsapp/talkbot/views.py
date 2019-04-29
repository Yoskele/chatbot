from django.shortcuts import render, redirect
from .import forms
from .models import ChattRoom

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.


def homepage(request):
	# bygg en post request få ordet av klienten
	# Lägg sedan in ordet i while lopen.
	return render(request, 'index.html')



def signup_view(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			print('Went thry')
			user = form.save()
			login(request, user)
			return redirect('talkbot:homepage')
	context = {
		'form':form
	}
	return render(request, 'signup.html', context)



def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# log in the user
			user = form.get_user()
			login(request, user)
			# Redirect User after Login in.
			if 'next' in request.POST:
				return redirect(request.POST.get)
			else:
				return redirect('talkbot:sendmessage')
	else:
		form = AuthenticationForm()
	return render(request, 'login.html', {'form':form})


def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('talkbot:login')

@login_required(login_url="/login/")
def sendmessage(request):
	if request.method == 'POST':
		form = forms.CreateMessage(request.POST)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			print('Before the Save')
			instance.save()
			print('After save')
			return redirect('talkbot:sendmessage')
	else:

		form = forms.CreateMessage()
	return render(request, 'chatbot.html', {'form':form })