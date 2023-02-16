from django.shortcuts import render
from .forms import UserRegistration
from .models import User
# Create your views here.

def show(request):
    fm = UserRegistration()
    params = {
        'form':fm
    }
    if request.method == 'POST':
        fm = UserRegistration(request.POST)

        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            fm = User(name=nm, email=em, password = pw)
            fm.save()
            print(nm)
            print(em)
            print(pw)

    return render(request, 'modelform/register.html', params)
