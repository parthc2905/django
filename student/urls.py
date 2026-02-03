from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.studentHome),
    path("Dashboard/", views.studentDashboard)
]