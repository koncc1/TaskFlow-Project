from django.shortcuts import render, HttpResponse
from django.shortcuts import render


def home(request):
    
    return render(request, "MAIN/home.html")
