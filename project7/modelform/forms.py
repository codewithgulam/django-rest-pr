from django import forms
from django.core import validators
from .models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'company', 'role']
        labels ={
            'name': 'Enter Name',
            'company': 'Company Name',
            'role': 'Current Role',
        }

        # error_messages ={  'name': {'required':'Naam likhna padega'},
        #     'company': {'required':'Company likhna padega'}
        # }
        widget = {
            'name':forms.TextInput(attrs={'class':'myclass', 'placeholder':'Enter your name'})
        }
