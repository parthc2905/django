from django.shortcuts import render

# Create your views here.

def studentHome(request):
    return render(request, 'student/studentHome.html')

def studentDashboard(request):
    student = {'name':'Parth chauhan','age': 23, 'city': 'ahemdabad'}
    return render(request, 'student/studentDashboard.html',student)

def studentMarks(request):
    marks = {'mark':[1,2,3,4,45,56]}
    return render(request, 'student/studentMarks.html', marks)

def studentCollege(request):
    colleges = {'college':'NEW LJ'}
    return render(request, 'student/studentCollege.html', colleges)

def studentEducation(request):
    educations = {'education' :"CSE(AIML)"}
    return render(request, 'student/studentEducation.html', educations)