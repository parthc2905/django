from django.shortcuts import render

# Create your views here.

def studentHome(request):
    return render(request, 'student/studentHome.html')

def studentDashboard(request):
    return render(request, 'student/studentDashboard.html')