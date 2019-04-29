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