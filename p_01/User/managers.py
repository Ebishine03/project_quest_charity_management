from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
   def create_user(self,email,username,name,password,**other):
      if not email:
         raise ValueError(_('Must provide an email address'))
      email=self.normalize_email(email)
      user=self.model(email=email,username=username,name=name,**other)
      user.set_password(password)
      user.save()
   def create_superuser(self,email,username,name,password,**other):
      other.setdefault('is_active',True)
      other.setdefault('is_staff',True)
      other.setdefault('is_superuser',True)
      if other.get('is_staff') is not True:
         raise ValueError('Superuser must be assigned to is staff=True')
      if other.get('is_superuser') is not True:
         raise ValueError('Super user must be assigned to is_superuser=true')
      return self.create_user(email,username,name,password,**other)
         
       