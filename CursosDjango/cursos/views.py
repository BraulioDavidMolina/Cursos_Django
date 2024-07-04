from django.shortcuts import render
from .models import Cursos

# Create your views here.
def viewCursos(request):
    cursos = Cursos.objects.all()
    return render(request, "cursos/cursos.html", {'cursos':cursos})


def consultar1(request):
    cursos=Cursos.objects.filter(nombre="Bootstrap")
    return render(request, "cursos/consultas.html", {'cursos':cursos})

def consultar2(request):
    cursos=Cursos.objects.filter(duracion=5)
    return render(request, "cursos/consultas.html", {'cursos':cursos})

def consultar3(request):
    cursos=Cursos.objects.filter(nombre__startswith="La")
    return render(request, "cursos/consultas.html", {'cursos':cursos})


def consultar4(request):
    cursos=Cursos.objects.filter(actividad__nombre__contains="Uso de")
    return render(request,"cursos/consultas.html", {'cursos':cursos})