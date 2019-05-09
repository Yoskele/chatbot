from django.contrib import admin

from .models import Chatroom, Message, Member, Upload, Profile_update, ArticlePost

# Register your models here.
admin.site.register(Chatroom),
admin.site.register(Message),
admin.site.register(Member),
admin.site.register(Upload),
admin.site.register(Profile_update),
admin.site.register(ArticlePost),
