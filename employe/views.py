from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def Home(request):

    ''' this is home page view this view will display list of all the employees'''

    employees = Employee.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(employees, 5)
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        employees = paginator.page(1)
    except EmptyPage:
        employees = paginator.page(paginator.num_pages)



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

    employee=Employee.objects.get(emp_id=emp_id)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html',{'employee':employee})

def DeleteView(request,emp_id):
    employee = Employee.objects.get(emp_id=emp_id)
    employee.delete()
    return redirect('/')


def search(request):
    q = request.GET["q"]
    employees = Employee.objects.filter(Q(name__contains=q) | Q(id__contains=q)) #(name_icontaions)
    # categories = Category.objects.filter(active=True)
    context = {"employees": employees,
               "title": q + " - search"}
    return render(request, "index.html", context)