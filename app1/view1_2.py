from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def display(request):
    return(HttpResponse("<h1> Hola soy la app1 segunda vista</h1>"))