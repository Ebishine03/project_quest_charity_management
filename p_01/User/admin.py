from django.contrib import admin
from django import forms
from .models import CustomUser
# from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','email', 'name', 'is_staff', 'is_superuser','phone','pin','password','gender','age','user_img')
    search_fields=['email']
    fieldsets=(
        None,{'fields':('email','username','name',)}
),('Permissions',{'fields':('is_staff','is_active')}),('Personal',{'fields':('age','phone','pin','place','user_type','user_img')}),

   
   
add_fields=(
    (None,{'classes':('wide'),
           'fields':('email','username','name','password1','password2','is_active','is_staff')})
)

admin.site.register(CustomUser,CustomUserAdmin)