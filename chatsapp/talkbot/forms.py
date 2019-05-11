from django import forms

from .models import Message, Member, Chatroom, Profile_update, ArticlePost

from django.forms import HiddenInput, TextInput

class CreateMessageForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ['text']
		# widgets = {
		# 	'room': forms.HiddenInput(),
		# }




class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile_update
		fields = ['name', 'lastname', 'age', 'city', 'country', 'description', 'profile_image']


class ArticlePost(forms.ModelForm):

	class Meta:
		model = ArticlePost
		fields = ['title', 'body', 'image']


class SearchFriendForm(forms.Form):
    friend = forms.CharField(max_length=50)