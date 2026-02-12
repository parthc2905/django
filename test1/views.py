from urllib import request
from django.shortcuts import render

# Create your views here.

def test1Home(request):
    return render(request, 'test1/test1Home.html')