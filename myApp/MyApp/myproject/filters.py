import django_filters
from .models import Employees
from django.db import models

class EmployeesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='filter_by_name')
    date_of_joining = django_filters.DateFilter(field_name='date_of_joining', lookup_expr='exact')

    class Meta:
        model = Employees
        fields = ['name', 'date_of_joining']

    def filter_by_name(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value)
        )
