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


    path('profile/delete/<int:chatroom_id>/', views.delete_message, name='delete_message'),

    path('update_profile_info/', views.update_profile_info, name='update_profile_info'),
    path('delete_profile_info/', views.delete_profile_info, name='delete_profile_info'),

    path('create_message/<int:chatroom_id>/', views.create_message, name="create"),
    path('create_post/', views.createpost, name="createpost"),
    path('create_like/<int:post_id>/', views.create_like, name="create_like"),

    path('allpostroom/', views.allpostroom, name="allpostroom"),

    # View your friend
    path('yourfriendwall/<int:friend_id>/', views.friend_view, name="friend_view"),
    
]

