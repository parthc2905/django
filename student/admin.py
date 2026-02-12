from django.contrib import admin
from .models import Student,Product,Course,StudentProfile,Category,Service
# Register your models here.


# To Show it to the Admin panel of the Django
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Course)
admin.site.register(StudentProfile)
admin.site.register(Category)
admin.site.register(Service)