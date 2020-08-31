from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .models import Employee
from .forms import EmployeeForm


def employee_list(request):
    employees = Employee.objects.all()

    page = request.GET.get('page', 1)  # create Paginator object with list of records and number of records per page.
    paginator = Paginator(employees, 5)  # to get list of records related to current page as follows
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(
            paginator.num_pages)  # If the parameter is higher than last page number then we will get EmptyPage.Instead
        # of displaying EmptyPage we have to display last page record
    return render(request, 'employees/employee_list.html', {'employees': employees})


def save_employee_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            employees = Employee.objects.all()
            data['html_employee_list'] = render_to_string('employees/includes/partial_employee_list.html', {
                'employees': employees
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
    else:
        form = EmployeeForm()
    return save_employee_form(request, form, 'employees/includes/partial_employee_create.html')


def employee_update(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
    else:
        form = EmployeeForm(instance=employee)
    return save_employee_form(request, form, 'employees/includes/partial_employee_update.html')


def employee_delete(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    data = dict()
    if request.method == 'POST':
        employee.delete()
        data['form_is_valid'] = True
        employees = Employee.objects.all()
        data['html_employee_list'] = render_to_string('employees/includes/partial_employee_list.html', {
            'employees': employees
        })
    else:
        context = {'employee': employee}
        data['html_form'] = render_to_string('employees/includes/partial_employee_delete.html', context, request=request)
    return JsonResponse(data)
