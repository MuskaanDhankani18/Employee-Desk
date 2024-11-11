from django import forms
from .models import Employees, Departments

class AddEmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ("name", "date_of_joining", "dept")
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'date_of_joining' : forms.DateInput(attrs={'class' : 'form-control', 'type': 'date'}),
            'dept' : forms.Select(attrs={'class' : 'form-control'}),
        }
    
    dept = forms.ModelChoiceField(
        queryset=Departments.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )