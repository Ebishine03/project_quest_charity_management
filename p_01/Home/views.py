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
def CreateUser(request):
     if request.method=='POST':
          form=CreateUserForm(request.POST)
          if form.is_valid():
               form.save()
               return HttpResponse('User Created')
          else:
               print(form.errors)
     form=CreateUserForm()
     return render(request,'register/user_registration.html',{'form':form})


