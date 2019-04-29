from django import forms
from django.forms import TextInput
from .models import ChattRoom

class Loginform(forms.Form):
	username = forms.CharField(max_length = 100, label="Username")
	password = forms.CharField(max_length = 100, label="Password", widget=forms.PasswordInput)
	


class CreateMessage(forms.ModelForm):

	class Meta:
		model = ChattRoom
		fields = ['message']