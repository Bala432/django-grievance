from django import forms
from app.models import UserInfo,Post,Publish

from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','last_name','email','username','password')


class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('roll_number','mobile_number')

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title','text')

class PublishForm(forms.ModelForm):

    class Meta():
        model = Publish
        fields = ('problem','details')



