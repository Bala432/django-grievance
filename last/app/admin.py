from django.contrib import admin
from app.models import Post,UserInfo,Publish

# Register your models here.
admin.site.register(Post)
admin.site.register(UserInfo)
admin.site.register(Publish)