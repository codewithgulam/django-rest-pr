from django import forms
from .models import User

def start_s(value):
    if value[0] != 's':
        raise forms.ValidationError("Namse Must Start With S.")
        
class UserCreation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),

        }
        