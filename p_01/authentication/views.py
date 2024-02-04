from django.shortcuts import render,redirect
from Employee.forms import LoginForm
from django.contrib.auth import authenticate, login, logout 

# Create your views here.
def user_login(request):
      if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)  
                user=username  
                return render(request,'main/home.html',{'user':username})
      else:
        form = LoginForm()
        return render(request, 'main/login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('login')