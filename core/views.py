from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.

def base(request):
    return render(request, "core/base.html")

def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")



def contac(request):
    return render(request, "core/contac.html")