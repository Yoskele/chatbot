from django.conf.urls import url

from django.urls import include, path

from django.contrib.auth.forms import UserCreationForm


from .import views
app_name= 'bot'
urlpatterns = [
	path('', views.help_bot, name='help_bot'),
	
]

