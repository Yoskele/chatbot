from django.db import migrations, models
from django.contrib.auth.models import User


# Create your models here.
class Message(models.Model):
    text = models.TextField(max_length=500)
    room = models.ForeignKey('Chatroom', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.text,self.room)

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chatroom = models.ForeignKey('Chatroom', on_delete=models.CASCADE)


    def __str__(self):
        return '{}, {}'.format(self.user,self.chatroom)


class Chatroom(models.Model):
    user = models.CharField(max_length=50)
    reciver = models.CharField(max_length=50, default="RandomUser")


    def __str__(self):
        return '{}, {}'.format(self.user,self.reciver)
