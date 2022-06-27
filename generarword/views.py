from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Bienvenido</h1>")

def principal(request):
    return render(request,'paginas/principal.html')
