from django.db import  models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=500)
    # So we can see till which chatroom it sends the message.
    chatroom = models.ForeignKey('Chatroom', on_delete=models.CASCADE)
    # See who Sent the Message.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Create a TimeStamp on the Message.
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}, {}'.format(self.text,self.chatroom)

class Member(models.Model):
    # See Who's Member on the ChatRoom.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey('Chatroom', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.user,self.chatroom)


class Chatroom(models.Model):
    # See Who Creatade the Room.
    created_by = models.CharField(max_length=50)
    # Name of the Room So we can See if the it Exist.
    name_of_chatroom = models.CharField(max_length=50)

    def __str__(self):
        return '{}, {}'.format(self.created_by,self.name_of_chatroom)


# class Public_chatroom(models.Model):
#     text = models.CharField(max_length=500)
#     member = models.


class Upload(models.Model):
    picture = models.ImageField(default=None, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return '{}, {}'.format(self.picture, self.user)