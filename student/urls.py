from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.studentHome),
    path("dashboard/", views.studentDashboard),
    path("marks/", views.studentMarks),
    path("college/", views.studentCollege),
    path("education/", views.studentEducation),
    path("serviceList/",views.serviceList,name="serviceList"),
    path("createService/",views.createService,name="createService"),    
]