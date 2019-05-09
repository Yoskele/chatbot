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


class Upload(models.Model):
    picture = models.ImageField(default=None, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.picture, self.user)


class Profile_update(models.Model):
    name = models.CharField(max_length=100, default='Name')
    lastname = models.CharField(max_length=100, default='Lastname')
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=100, default='City')
    country = models.CharField(max_length=100, default='Country')
    profile_image = models.ImageField(default='default.jpg', blank=True)
    description = models.CharField(max_length=200, default='Description')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.name, self.lastname, self.city, self.country, self.profile_image)

class ArticlePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpeg')
    like = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.user, self.title, self.body, self.date_created, self.like)
