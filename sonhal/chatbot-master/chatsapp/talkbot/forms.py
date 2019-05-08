from django import forms

from .models import Message, Member, Chatroom, Upload

from django.forms import HiddenInput

class CreateMessageForm(forms.ModelForm):
	text = forms.CharField(label='')
	
	class Meta:
		model = Message
		fields = ['text']
		# widgets = {
		# 	'room': forms.HiddenInput(),
		# }

class UploadForm(forms.ModelForm):

	class Meta:
		model = Upload
		fields = ['picture']