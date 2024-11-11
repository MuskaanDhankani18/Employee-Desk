from django.contrib import admin
from .models import Employees, Departments
# Register your models here.

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ['name','email']

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_joining', 'dept']
