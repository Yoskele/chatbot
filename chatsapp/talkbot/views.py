from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import Chatroom, Message, Member, Upload, Profile_update, ArticlePost
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
#Flash message
from django.contrib import messages
# For Game Room.
import random


# Works
def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('Created a new User')
            login(request, user)
            return redirect('talkbot:profile')
    context = {
        'form':form
    }
    return render(request, 'signup.html', context)



# Works
def logout_view(request):
        logout(request)
        return redirect('talkbot:login')


# Works
def contact_us(request):
    return render(request, 'contact_us.html')


# Works 
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            print('form is valid')
            user = form.get_user()
            login(request, user)
            # Redirect User after Login in.
            if 'next' in request.POST:
                return redirect(request.POST.get)
            else:
                return redirect('talkbot:profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

@login_required(login_url="/")
def profile(request):
    # Get all User in dataBase Exclude Admin and the User. Display at html template friend list.
    users = User.objects.all().exclude(username='admin').exclude(username=request.user)
    # Get the user profile 
    profile = Profile_update.objects.filter(user=request.user)
    # Get user post
    print(profile)
    posts = ArticlePost.objects.filter(user=request.user).order_by('-date_created')

    form_search_friend = forms.SearchFriendForm()

    context = {
        'form_search_friend': form_search_friend,
        'users': users,
        'profile': profile,
        'posts': posts

    }
    return render(request, 'user_profile.html', context)


def friend_view(request, friend_id):
    profile_friend = Profile_update.objects.filter(user=friend_id)

    posts = ArticlePost.objects.all().filter(user=friend_id).order_by('-date_created')
    print(posts)
    context = {
        'profile_friend': profile_friend,
        'posts': posts
    }
    return render(request, 'friend_view.html', context)

@login_required(login_url="/")
def update_profile_info(request):
    form = forms.ProfileForm()
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_user = form.save(commit=False)
            profile_user.user = request.user
            profile_user.save()
            print('after Save')
            return redirect('talkbot:profile')
    context = {
        'form': form
    }
    return render(request, 'profile_update.html', context)

@login_required(login_url="/")
def delete_profile_info(request):
    Profile_update.objects.filter(user=request.user).delete()
    return redirect('talkbot:update_profile_info')

@login_required(login_url="/")
def delete_message(request, chatroom_id):
    # Delete his messages in that room he is in...
    text = Message.objects.filter(user_id=request.user.id).filter(chatroom=chatroom_id).delete()
    #Flash message that the messages are deleted.
    messages.add_message(request, messages.INFO, 'Your Messages Are Deleted')
    return redirect('talkbot:profile')



def allpostroom(request):
    allposts = ArticlePost.objects.all().order_by('-date_created')
    print(allposts)
    context = {
        'allposts': allposts
    }
    return render(request, 'all_post_room.html', context)




def member(request, friend_id):
    # Check if User and his Friend are Members to a Chatroom.
    memberroom = Chatroom.objects.filter(member__user=request.user).filter(member__user=friend_id)
    print('Before If Statment')
    print(friend_id)
    if len(memberroom) == 0:
        create_room = Chatroom(created_by=request.user, name_of_chatroom='MushroomHunt')
        create_room.save()
        # Get the last room in the list that we just created.
        new_room = Chatroom.objects.last()
        # Push in Members to the  last Room we just created.
        # Pushed my ID First
        member = Member(chatroom=new_room, user=request.user)
        # Storing Friends ID in Member.
        member_friend = Member(chatroom=new_room, user_id=friend_id)
        member.save()
        member_friend.save()
        #Flas Message That says it creatade a room.
        messages.add_message(request, messages.SUCCESS, 'Enjoy your First Conversation')
        return redirect('talkbot:chatroom', chatroom_id=new_room.id)
    else:
        print(' Not Empty')
        # Get the list of members.
        exist = Chatroom.objects.filter(member__user=request.user).filter(member__user=friend_id)
        # Loop around to see what id is on the chatroom.
        for i in exist:
            chatroom = Chatroom.objects.filter(member__user__id=friend_id).filter(pk=i.id).first()
            if chatroom != None:
                break
        return redirect('talkbot:chatroom', chatroom_id=chatroom.id)

@login_required(login_url="/")
def chatroom(request, chatroom_id):
    chatroom = Chatroom.objects.get(pk=chatroom_id)
    texts = Message.objects.all().filter(chatroom=chatroom_id)
    form = forms.CreateMessageForm()
    context = {
        'chatroom': chatroom,
        'texts': texts,
        'form': form,
    } 
    return render(request, 'chatroom.html', context)

@login_required(login_url="/")
def create_message(request, chatroom_id):
    form = forms.CreateMessageForm()
    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
    if request.method == 'POST':
        form = forms.CreateMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.chatroom = chatroom
            message.save()
            return redirect('talkbot:chatroom', chatroom_id=chatroom_id)
    context = {
        'form':form
    }
    return render(request, 'chatroom.html', context)  

@login_required(login_url="/")
def create_like(request, post_id):
    like = ArticlePost.objects.get(pk=post_id)
    like.like += 1
    like.save()
    print(like)
    return redirect('talkbot:profile')

@login_required(login_url="/")
def createpost(request):
    form = forms.ArticlePost()
    if request.method == 'POST':
        form = forms.ArticlePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            print('Post Saved')
            return redirect('talkbot:profile')
    context = {
        'form': form
    }
    return render(request, 'createpost.html', context)


def find_friend(request):
    user_profiles = Profile_update.objects.all()
    form = forms.SearchFriendForm()
    if request.method == 'POST':
        form = forms.SearchFriendForm(request.POST)
        if form.is_valid():
            friend = form.cleaned_data['friend']
            friend_id = User.objects.get(username=friend).pk
            friend_profile = Profile_update.objects.get(user_id=friend_id)
            context = {
                'friend': friend,
                'user_profiles': user_profiles,
                'friend_profile': friend_profile,
            }
            return render(request, 'find_friend.html', context)



def game_room(request):
    # Pick a player.
    return render(request, 'game_room.html')


def game_room_outcome(request, number):
    print(number)
    context = {
        'number': number
    }
    return render(request, 'game_room.html', context)



def roll_dice(request):
    roll_dice_value = random.randint(1,10)
    return redirect('talkbot:game_room_outcome', number=roll_dice_value)


