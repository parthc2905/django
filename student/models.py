from django.db import models

# student Database
class Student(models.Model):
    studentName = models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    #meta class
    class Meta:
        db_table = "student"   #table name

#product db

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20, null=True)
    productStatus = models.BooleanField(default=True)

    class Meta:
        db_table = "product"


#course db

class Course(models.Model):
    courseName = models.CharField(max_length=100)
    courseCode = models.PositiveIntegerField()

    class Meta:
        db_table = "course"

