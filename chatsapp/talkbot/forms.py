from django import forms
from django.forms import TextInput
from .models import ChattRoom


class CreateMessage(forms.ModelForm):

	class Meta:
		model = ChattRoom
		fields = ['message']
