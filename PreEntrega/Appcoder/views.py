from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Curso, Estudiante, Profesor, Entregable

def inicio(request):
    return render(request, "inicio.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(request, "resultadosBusqueda.html", {"cursos": cursos, "camada": camada})
    else:
        return render(request, "inicio.html")
 

def profesores(request):
    if request.method == 'GET':
        # SHOW INTERFACE
        return render(request, 'profesores.html')
    else:
        Profesor.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'], profesion=request.POST['profesion'])    
        return redirect('inicio')
 
def cursos(request):
    if request.method == 'GET':
        # SHOW INTERFACE
        return render(request, 'cursos.html')
    else:
        Curso.objects.create(nombre=request.POST['nombre'], camada=request.POST['camada'])    
        return redirect('inicio')

def estudiantes(request):
    if request.method == 'GET':
        # SHOW INTERFACE
        return render(request, 'estudiantes.html')
    else:
        Estudiante.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'], email=request.POST['email'])    
        return redirect('inicio')

def entregables(request):
    if request.method == 'GET':
        # SHOW INTERFACE
        return render(request, 'entregables.html')
    else:
        booleano = False
        if 'entregado' in request.POST:
            booleano = bool(request.POST['entregado'])
            Entregable.objects.create(nombre=request.POST['nombre'], fechaDeEntrega=request.POST['fechaDeEntrega'], entregado=booleano) 
            return redirect('inicio')
        else:
            Entregable.objects.create(nombre=request.POST['nombre'], fechaDeEntrega=request.POST['fechaDeEntrega'], entregado=booleano) 
            return redirect('inicio')