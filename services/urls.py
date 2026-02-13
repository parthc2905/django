from django.urls import path
from . import views

urlpatterns = [
    path('servicesList/', views.servicesList, name='serviceList'),
    path('createServices/', views.createServices, name='createServices'),
    path('deleteService/<int:id>', views.deleteService, name='deleteService'),
    path('updateService/<int:id>', views.updateService, name='updateService'),
]