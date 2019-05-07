from django import forms


class Question(forms.Form):
	question_text = forms.CharField(max_length=100)
