from django.shortcuts import render
from .forms import CreateUserForm,UserCreationForm
from django.http import HttpResponse

# Create your views here.
def home(request):
     return render(request,'main/home.html')
     # return render(request,'main/login.html')

def login(request):
     return render(request,'main/login.html')

def reset(request):

     return render(request,'main/forgot_password.html')



