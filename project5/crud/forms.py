from django import forms

class Employee(forms.Form):
    name = forms.CharField(max_length=20)
    company = forms.CharField()
    employee_id = forms.IntegerField()
    