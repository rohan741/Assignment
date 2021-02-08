from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeCreate
from django.http import HttpResponse

# view written to show all the employee data save in database
def index(request):
    empall = Employee.objects.all()
    return render(request, 'employee/employeelist.html', {'empall': empall})

# view function written to add new employee data
def upload(request):
    upload = EmployeeCreate()
    if request.method == 'POST':
        upload = EmployeeCreate(request.POST)
        if upload.is_valid():
		
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'employee/addemployee.html', {'upload_form':upload})

# View function is written to update or modify present employee data of particular employee
def update_employee(request, employee_id):
    employee_id = int(employee_id)
    try:
        employee_sel = Employee.objects.get(id = employee_id)
    except Employee.DoesNotExist:
        return redirect('index')
    employee_form = EmployeeCreate(request.POST or None, instance = employee_sel)
    if employee_form.is_valid():
       employee_form.save()
       return redirect('index')
    return render(request, 'employee/addemployee.html', {'upload_form':employee_form})

# View function is written to delete data of any employee permanantly, deleted data can't be undone
def delete_employee(request, employee_id):
    employee_id = int(employee_id)
    try:
        employee_sel = Employee.objects.get(id = employee_id)
    except Employee.DoesNotExist:
        return redirect('index')
    employee_sel.delete()
    return redirect('index')
	