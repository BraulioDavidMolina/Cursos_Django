from django.shortcuts import render, HttpResponse

# Create your views here.
def PaginaPrincipal(request):
    return render(request, "contenido/home.html")

def cursos(request):
    return render(request, "contenido/cursos.html")

def contacto(request):
    return render(request, "contenido/contacto.html")

def formulario(request):
    return render(request, "contenido/formulario.html")

def ejemplo(request):
    return render(request, "contenido/ejemplo.html")