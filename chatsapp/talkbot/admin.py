from django.contrib import admin

from .models import Chatroom, Message, Member

# Register your models here.
admin.site.register(Chatroom),
admin.site.register(Message),
admin.site.register(Member),