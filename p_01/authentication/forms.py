
from User.models import  CustomUser
from django.contrib.auth.forms import AuthenticationForm

from django.db import models

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput)
class LoginForm(AuthenticationForm):
   class Meta:
      model=CustomUser
      fields=['username','password']