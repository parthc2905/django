from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    salary = models.IntegerField()
    join_date = models.DateField()
    post = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
    
    def __str__(self):
        return self.name

class EmployeeCourse(models.Model):
    name = models.CharField(max_length=100)
    fee = models.IntegerField()
    duration = models.IntegerField()
    class Meta:
        db_table = "employeecourse"
    def __str__(self):
        return self.name
