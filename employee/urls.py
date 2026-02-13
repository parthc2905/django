from django.urls import path
from . import views

urlpatterns = [
    path('employeeList/', views.employeeList, name='employeeList'), # name is used for direct calling of url.
    path('employeeFilter/', views.employeeFilter, name='employeeFilter'),

    path('createEmployeeWithForm/',views.createEmployeeWithForm,name="createEmployeeWithForm"),
    path('createCourse/',views.createCourse),

    #path('deleteEmployee/',views.deleteEmployee,name="deleteEmployee")
    path("deleteEmployee/<int:id>",views.deleteEmployee,name="deleteEmployee"),  # <int:id> --> url parameter. it returns id when form is submitted.
    path("filterEmployee/",views.filterEmployee,name="filterEmployee"),
    path("ascEmployee/",views.ascendingEmployee,name="ascendingEmployee"),
    path("dscEmployee/",views.desendingEmployee,name="desendingEmployee"),
]
