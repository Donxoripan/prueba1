from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index (request):
    return HttpResponse("<h1>so el index de la app3 </h1>")

def vista1(request):
    html="<h1>so el  vista de la app3 </h1>"
    