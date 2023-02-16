from django.shortcuts import render
from .forms import UserForm
from .models import User
# Create your views here.

def show(request):
    fm = UserForm()
    param = {
        'form': fm
    }
    if request.method =='POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            
            nm = fm.cleaned_data['name']
            cp = fm.cleaned_data['company']
            rl = fm.cleaned_data['role']

            print(nm)
            print(cp)
            print(rl)
            new_user = User(name=nm, company = cp, role = rl)
            new_user.save()
    return render(request, 'modelform/index.html' , param)