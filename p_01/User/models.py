from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser,PermissionsMixin):
   
   gen=(('M','male'),('f','female'))
   USER_TYPE_CHOICES = (
        ('user', 'user'),
        ('employee', 'employee'),
        ('admin', 'admin'),

        ('volunteer', 'volunteer'),)
   name=models.CharField(max_length=50)
   username=models.CharField(max_length=50,unique=True)
   
   phone=models.CharField(max_length=12)
   email=models.EmailField(max_length=50,unique=True)
   place=models.CharField(max_length=100)
   pin=models.IntegerField(null=True)
   age=models.IntegerField(null=True)
   gender=models.CharField(choices=gen,max_length=10)
   user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='user')
   is_active=models.BooleanField(default=False)
   is_staff=models.BooleanField(default=False)
   start_date=models.DateTimeField(default=timezone.now)
   user_img=models.ImageField(upload_to='user_image',blank=True)
   objects=CustomUserManager()
   USERNAME_FIELD='email'
   REQUIRED_FIELDS=['username','name']

   def __str__(self):
      return self.username
