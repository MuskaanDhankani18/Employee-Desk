from rest_framework import serializers
from .models import Departments, Employees

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    departments = DepartmentsSerializer()

    class Meta:
        model = Employees
        fields = '__all__'
