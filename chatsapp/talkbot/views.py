from django.shortcuts import render, redirect
from .import forms
from .models import Chatroom, Message, Member
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

#Flash message
from django.contrib import messages



def homepage(request):
    # bygg en post request få ordet av klienten.
    # Lägg sedan in ordet i while lopen.
    users = User.objects.all()
    member = Member.objects.all()
    context = {
        'users':users,
        'member': member
    }
    return render(request, 'index.html', context)



def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print('Went thry')
            user = form.save()
            login(request, user)
            return redirect('talkbot:homepage')
    context = {
        'form':form
    }
    return render(request, 'signup.html', context)



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('talkbot:login')

def profile(request):
    return render(request, 'user_profile.html')


def contact_us(request):
    return render(request, 'contact_us.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            # Redirect User after Login in.
            if 'next' in request.POST:
                return redirect(request.POST.get)
            else:
                return redirect('talkbot:homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})




def member(request, slug):
    print(slug)
    print(request.user)
    # filter gives a list with all the values that match
    chatrooms = Chatroom.objects.filter(reciver=slug).filter(user=request.user)
    if len(chatrooms) == 0:
        user = request.user
        room = Chatroom(reciver=slug, user=user)
        room.save()
        print(room.id)
        # Flas Message That says it creatade a room.
        messages.add_message(request, messages.SUCCESS, 'Enjoy your First Conversation with {}'.format(slug))
        return redirect('talkbot:chatroom', id=room.id)
    else:
        # Bring the first index of the Chatroom list.
        chatroom = chatrooms[0]
        print('Room id', chatroom.id)
        return redirect('talkbot:chatroom', id=chatroom.id) 
# # to check if there are a current chat room with user and reciver
# # TEST INTERNET groups = Group.objects.filter(player=p1).filter(player=p2)
#     chatroom = Chatroom.objects.filter(username=username).filter(reciver=reciver)
#     mario wants to talk in a room so he clicks on a tag that's' on lugi.
#      Does the room exist? if yes lead to room id. if no create an room id.
#      chatroom = Chatroom.objects.get('luigi', 'mario')

#      ska vara något sånt här.
#      chatroom.objects.get( user whos online and user he wants to talk to.)
#      if its none, create a new chatroom, alltså inne i databasen ingen data i kolumen.
#      if its not none redirect him to the room id... 



# Chatroom 
def chatroom(request, id):
    chatroom = Chatroom.objects.get(pk=id)
    return render(request, 'chatroom.html')



# Chatbot/
@login_required(login_url="/login/")
def sendmessage(request):
    messages = Chatroom.objects.all()
    f = forms.CreateMessage()
    if request.method == 'POST':
        f = forms.CreateMessage(request.POST)
        if f.is_valid():
            instance = f.save(commit=False)
            instance.user = request.user
            print('Before the Save')
            instance.save()
            print('After save')
            return redirect('talkbot:sendmessage')

    context = {
        'form': f,
        'messages': messages
    }

    return render(request, 'chatbot.html', context)



