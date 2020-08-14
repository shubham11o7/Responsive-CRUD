from django.shortcuts import render,redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def Home(request):

    ''' this is home page view this view will display list of all the employees'''

    employees = Employee.objects.all()
    page = request.GET.get('page', 1) # create Paginator object with list of records and number of records per page.
    paginator = Paginator(employees, 5) #to get list of records related to current page as follows
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)# If the parameter is higher than last page number then we will get EmptyPage.Instead
                                        #of displaying EmptyPage we have to display last page records
    return render(request,'index.html',{ 'employees': employees })



def CreateView(request):

    ''' this view helps us creating new user entries'''

    form = EmployeeForm()
    if request.method =='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'create.html', {'form': form})

def UpdateView(request,emp_id):

    ''' this function will help us updating the list'''

    employee=Employee.objects.get(emp_id=emp_id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html',{'employee':employee})

def DeleteView(request,emp_id):

    ''' will delete an entries from list'''

    employee = Employee.objects.get(emp_id=emp_id)
    employee.delete()
    return redirect('/')


#