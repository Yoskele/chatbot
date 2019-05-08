from django.conf.urls import url

from django.urls import include, path

from django.contrib.auth.forms import UserCreationForm


from .import views



app_name= 'talkbot'
urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('contact_us/', views.contact_us, name="contact_us"),

    path('member/<int:friend_id>/', views.member, name='member'),
    path('chatroom/<int:chatroom_id>/', views.chatroom, name='chatroom'),
    path('createmessage/<int:chatroom_id>/', views.create_message, name="create"),
]

