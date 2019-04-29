from django.shortcuts import render, redirect
from .forms import forms,Loginform
from .models import ChattRoom
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
			
			return render(request, "login.html",context)

		
		login(request,user)
		return redirect('homepage')


	return render(request, 'login.html', {'form': form})



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






@login_required
def sendmessage(request):
	if request.method == 'POST':
		form = forms.CreateMessage(request.POST)
		if form.is_valid():
			print('YooooooooooooooooS')
			# Save Article to db
			instance = form.save(commit=False)
			# Saving the user to the article he uploads.
			instance.author = request.user
			instance.save()
			return redirect('talkbot:chatbot')
	else:

		form = forms.CreateMessage()
	return render(request, 'chatbot.html', {'form':form })