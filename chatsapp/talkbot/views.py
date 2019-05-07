from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import Chatroom, Message, Member
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required

#Flash message
from django.contrib import messages



def profile(request):
    # Get all User in dataBase Exclude Admin and the User. Display at html template friend list.
    users = User.objects.all().exclude(username='admin').exclude(username=request.user)

    context = {
        'users':users
    }
    return render(request, 'user_profile.html', context)


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



def member(request, friend_id):
    # Check if User and his Friend are Members to a Chatroom.
    memberroom = Chatroom.objects.filter(member__user=request.user).filter(member__user=friend_id)
    print('Before If Statment')
    print(friend_id)
    if len(memberroom) == 0:
        print('Empty list.')
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

        print('roomSaved and past the if statment.')
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



def chatroom(request, chatroom_id):
    # Gets all Messages from that group that this user wrote.
    #user_messages = Message.objects.all().filter(chatroom=chatroom).filter(user=request.user)
    # Get all Members from the Chatroom id. And Exclude means take of userOnline from the list.
    #other_members = Member.objects.filter(chatroom=chatroom).exclude(user=request.user)
    # Get the friend First index from Members.
    #friend = other_members[0].user
    # Gets all Messages from that group that this Friend wrote. Searching my friend Instance who has a user_id inside.
    #friend_messages = Message.objects.filter(chatroom=chatroom).filter(user=friend)
    chatroom = Chatroom.objects.get(pk=chatroom_id)
    texts = Message.objects.all().filter(chatroom=chatroom_id)
    form = forms.CreateMessageForm()
    context = {
        #'user_messages': user_messages,
        #'friend_messages': friend_messages,
        'chatroom': chatroom,
        'texts': texts,
        'form': form,
    } 
    return render(request, 'chatroom.html', context)


def create_message(request, chatroom_id):
    form = forms.CreateMessageForm()
    chatroom = get_object_or_404(Chatroom, pk=chatroom_id)
    print('Before Post')
    if request.method == 'POST':
        form = forms.CreateMessageForm(request.POST)
        if form.is_valid():
            print('Before Validation')
            message = form.save(commit=False)
            message.user = request.user
            print(message.user)
            message.chatroom = chatroom
            print(chatroom_id)
            message.save()
            print('Message Saved')
            return redirect('talkbot:chatroom', chatroom_id=chatroom_id)
    context = {
        'form':form
    }
    return render(request, 'chatroom.html', context)  


# def help_center(request):
#     form = forms.HelpForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'help_center.html', context)



# def help_question(request):
#     form = form.HelpForm()
#     if request.method == 'POST':
#         form = HelpForm(request.POST)
#         if form.is_valid():
#             question_text = form.cleaned_data['question_text']
#             print(question_text)
#         return render(request, 'help_center.html', context)
#     context = {
#         'form': form
#     }
#     return render(request, 'help_center.html', context)