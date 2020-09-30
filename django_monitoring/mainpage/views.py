from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'mainpage.html')

def mapview(request):
    return render(request, 'map.html')

# Create your views here.
