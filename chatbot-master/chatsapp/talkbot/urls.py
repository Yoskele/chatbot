from django.conf.urls import url
from django.urls import include, path
from . import views
from django.contrib.auth.forms import UserCreationForm



app_name = 'talkbot'
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login', views.loginview, name="loginview"),
    path('signup/', views.signup_view, name="signup"),
    path('chatbot/', views.sendmessage, name="sendmessage"),
]

