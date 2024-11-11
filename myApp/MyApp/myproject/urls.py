from django.urls import path
from .views import Home, Add_Employees, Delete_Employees, Edit_Employees

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('add-employees/', Add_Employees.as_view(), name='add-employees'),
    path('delete-employees/', Delete_Employees.as_view(), name='delete-employees'),
    path('edit-employees/<id>/', Edit_Employees.as_view(), name='edit-employees'),
]