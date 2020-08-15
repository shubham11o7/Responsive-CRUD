from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('emp_id','firstname','lastname','emp_address','emp_sal')
