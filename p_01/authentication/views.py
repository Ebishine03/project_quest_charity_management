
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                print('error') 
    else:
       pass
    form = LoginForm()
    return render(request,'main/login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('home')