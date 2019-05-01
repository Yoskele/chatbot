from django.conf.urls import url

from django.urls import include, path

from django.contrib.auth.forms import UserCreationForm


from .import views


app_name= 'talkbot'
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('chatbot/', views.sendmessage, name="sendmessage"),
    path('chatroom/<int:id>/', views.chatroom, name="chatroom"),
    path('chatroom/<slug>/', views.member, name="member"),
    path('profile/', views.profile, name="profile"),
    path('contact_us/', views.contact_us, name="contact_us"),


]

