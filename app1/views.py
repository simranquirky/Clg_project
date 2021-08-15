from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'a.html' ,{'link1':'http://127.0.0.1:8000/login/', 'link2':'http://127.0.0.1:8000/register/'})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')