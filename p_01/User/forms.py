# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'name', 'phone', 'place', 'pin', 'age', 'gender', 'user_img', 'password1', 'password2']
   
