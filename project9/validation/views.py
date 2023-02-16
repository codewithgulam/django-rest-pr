from django.shortcuts import render
from .forms import UserCreation
# Create your views here.
from .models import User
from django.contrib import messages


def homeView(request):
    fd = UserCreation()
    if request.method == 'POST':
        fd = UserCreation(request.POST)
        if fd.is_valid():
            un = fd.cleaned_data['username']
            pw = fd.cleaned_data['password']
            reg = User(username=un, password=pw)
            reg.save()
            messages.add_message(request, messages.SUCCESS, "Your account has been Created!!")
            # messages.add_message(request, messages.INFO, "Log In!!")
        fd = UserCreation()

    else:
        fd = UserCreation()
    user_obj = User.objects.all()
    params= {
        'form' : fd ,
        'datas' : user_obj
    }

    return render(request,'validation/home.html',params)