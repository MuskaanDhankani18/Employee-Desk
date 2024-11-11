from django.shortcuts import render, redirect
from django.views import View
from .models import Employees, Departments
from .forms import AddEmployeesForm
from .filters import EmployeesFilter
from rest_framework import viewsets, filters
from .serializers import DepartmentsSerializer, EmployeesSerializer
from django_filters.rest_framework import DjangoFilterBackend


class Home(View):
    def get(self, request):
        emp_filter = EmployeesFilter(request.GET, queryset=Employees.objects.all())
        emp_data = emp_filter.qs
        return render(request, 'home.html', {'empdata' : emp_data, 'filter' : emp_filter})
    
class Add_Employees(View):
    def get(self, request):
        fm = AddEmployeesForm()
        return render(request, 'addEmployees.html', {'form' : fm})
    
    def post(self, request):
        fm = AddEmployeesForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request, 'addEmployees.html', {'form' : fm})

class Delete_Employees(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        empdata = Employees.objects.get(id = id)
        empdata.delete()
        return redirect('/')
    
class Edit_Employees(View):
    def get(self, request, id):
        emp = Employees.objects.get(id = id)
        fm = AddEmployeesForm(instance=emp)
        return render(request, 'editEmployees.html', {'form' : fm})
    
    def post(self, request, id):
        emp = Employees.objects.get(id = id)
        fm = AddEmployeesForm(request.POST, instance=emp)
        if fm.is_valid():
            fm.save()
            return redirect('/')

class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = EmployeesFilter

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['name']  # Adjusted filter fields

