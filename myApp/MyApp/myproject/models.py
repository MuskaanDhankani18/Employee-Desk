from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Employees(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    date_of_joining = models.DateField()
    dept = models.ForeignKey(Departments, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name