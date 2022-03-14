from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','password1', 'password2','height','weight','age']


