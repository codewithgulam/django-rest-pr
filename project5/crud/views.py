from django.shortcuts import render
from .forms import Employee
from .models import Employee_data
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def home(request):
    fd = Employee()
    context = {
        'form': fd
    }

    if request.method == 'POST':
        form = Employee(request.POST)
        if form.is_valid():
            new_employee = Employee_data()
            new_employee.name = form.cleaned_data['name']
            new_employee.company = form.cleaned_data['company']
            new_employee.employee_id = form.cleaned_data['employee_id']
            new_employee.save()
            return HttpResponse("REgistration completed")
    return render(request, 'crud/index.html', context)

        
def show(request):

    employee = Employee_data.objects.all()

    return render(request, 'crud/show.html',{'employee': employee} )


def delete(request, id):
    employee = Employee_data.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect('/')


def update(request, id):
    fd = Employee_data.objects.get(id=id)
    context = {
        'form': fd
    }
    return render(request, 'crud/update.html', context)

def updatedata(request, id):

    if request.method == 'POST':
        nm = request.POST['name']
        comp = request.POST['company']
        e_id = request.POST['employee_id']

        update_emp = Employee_data.objects.get(id=id)
        update_emp.name = nm
        update_emp.company = comp
        update_emp.employee_id= e_id
        # update_emp = Employee_data(id=id,name=nm, company=comp, employee_id = e_id )
        update_emp.save()

    return HttpResponseRedirect('/')