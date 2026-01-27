from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Hello")

# def AboutUs(request):
#     return HttpResponse("AboutUs")

def AboutUs(request):
    return render(request, 'aboutus.html')

def ContactUs(request):
    return render(request, 'contactus.html')

def home(request):
    return render(request, 'home.html')

def movies(request):
    return render(request, 'movies.html')

def show(request):
    return render(request, 'show.html')

def news(request):
    return render(request, 'news.html')