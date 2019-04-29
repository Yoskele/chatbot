from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'talkbot'
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('login', views.loginview, name="loginview")
]
