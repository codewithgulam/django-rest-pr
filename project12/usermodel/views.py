from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def SignUp(request):
    
    if request.method =='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Account Created Successfully with usercreationform')
    else:
        fm = SignUpForm()
   
    return render(request, 'usermodel/index.html', {'form':fm})


# Login View
def user_login(request):

    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            pw = fm.cleaned_data['password']
            user = authenticate(username=uname,password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'usermodel/login.html', {'form':fm})
    

    # profile view

def user_profile(request):
    return render(request, 'usermodel/profile.html')