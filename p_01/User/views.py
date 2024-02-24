from django.shortcuts import render,redirect
from User.forms import CustomUserSignUpForm
from django.contrib.auth import login

def users_signup(request):
    if request.method == 'POST':
        form = CustomUserSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'user' 
            user.is_active=True
            user.save()
            print('done')
            login(request, user)
            return redirect('home')

    else:
        form = CustomUserSignUpForm()

    return render(request,'register/user_registration.html',{'form':form})
                  