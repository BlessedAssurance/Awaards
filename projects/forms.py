from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
