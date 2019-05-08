from django.contrib import admin

from .models import Chatroom, Message, Member, Upload

# Register your models here.
admin.site.register(Chatroom),
admin.site.register(Message),
admin.site.register(Member),
admin.site.register(Upload),

