from django import forms

from .models import Message, Member, Chatroom

from django.forms import HiddenInput

class CreateMessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ['text']
		# widgets = {
		# 	'room': forms.HiddenInput(),
		# }
