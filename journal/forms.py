from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import TextInput,PasswordInput
from django.forms import ModelForm
from . models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class ThoughtForm(ModelForm):
    class Meta:
        model = Thoughts
        fields = ['title','content']
        exclude = ['user']

class UpdateUSerForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ['username','email',]
        exclude = ['password1','password2']

class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    class Meta:
        model = Profile
        fields = ['profile_pic']