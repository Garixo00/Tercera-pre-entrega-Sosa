from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from appproyecto3pe.models import Asesor

# Create your views here.
def inicio(request):
    return render(request,"appproyecto3pe/inicio.html")

def asesores(request):
    return render(request,"appproyecto3pe/asesores.html")

def evaluadores(request):
    return render(request,"appproyecto3pe/evaluadores.html")

def evaluaciones(request):
    return render(request,"appproyecto3pe/evaluaciones.html")
    
def asesor_formulario(request):
    if request.method == 'POST':
        asesor = Asesor(nombre=request.POST['nombre'],apellido=request.POST['apellido'],id_asesor=request.POST['id_asesor']).save()
        
        return render(request,"appproyecto3pe/asesor_registrado.html")
    
    return render(request,"appproyecto3pe/asesor_formulario.html")

def asesorregistrado(request):
    return render(request,"appproyecto3pe/asesor_registrado.html")

def busquedaasesor(request):
    return render(request,"appproyecto3pe/busquedaasesor.html")

def buscar_as(request):
    if request.GET["id_asesor"]:
        id_asesor = request.GET["id_asesor"]
        nombres = Asesor.objects.filter(id_asesor__icontains=id_asesor)
        apellidos = Asesor.objects.filter(id_asesor__icontains=id_asesor)
        
        return render(request,"appproyecto3pe/buscarasesor.html", {"nombres":nombres,"apellidos":apellidos,"id_asesor":id_asesor})
    else:
        return render(request,"appproyecto3pe/buscarasesorno.html")

def evaluador_formulario(request):
    if request.method == 'POST':
        evaluador = Evaluador(nombre=request.POST['nombre'],apellido=request.POST['apellido'],id_evaluador=request.POST['id_evaluador']).save()
        
        return render(request,"appproyecto3pe/evaluador_registrado.html")
    
    return render(request,"appproyecto3pe/evaluador_formulario.html")

def evaluadorregistrado(request):
    return render(request,"appproyecto3pe/evaluador_registrado.html")

def busquedaevaluador(request):
    return render(request,"appproyecto3pe/busquedaevaluador.html")

def buscar_evdor(request):
    if request.GET["id_evaluador"]:
        id_evaluador = request.GET["id_evaluador"]
        nombres = Evaluador.objects.filter(id_evaluador__icontains=id_evaluador)
        apellidos = Evaluador.objects.filter(id_evaluador__icontains=id_evaluador)
        return render(request,"appproyecto3pe/buscarevaluador.html", {"nombres":nombres,"apellidos":apellidos,"id_evaluador":id_evaluador})
    else:
        return render(request,"appproyecto3pe/buscarevaluadorno.html")
    
def evaluacion_formulario(request):
    if request.method == 'POST':
        evaluacion = Evaluacion(id_evaluador=request.POST['id_evaluador'],id_asesor=request.POST['id_asesor'],id_evaluacion=request.POST['id_evaluacion'],fecha_evaluacion=request.POST['fecha_evaluacion']).save()
        
        return render(request,"appproyecto3pe/evaluacion_registrada.html")
    
    return render(request,"appproyecto3pe/evaluaciones_formulario.html")

def evaluacionregistrada(request):
    return render(request,"appproyecto3pe/evaluacion_registrada.html")

def busquedaevaluacion(request):
    return render(request,"appproyecto3pe/busquedaevaluacion.html")

def buscar_evalu(request):
    if request.GET["id_evaluacion"]:
        id_evaluacion = request.GET["id_evaluacion"]
        id_evaluadores = Evaluacion.objects.filter(id_evaluacion__icontains=id_evaluacion)
        id_asesores = Evaluacion.objects.filter(id_evaluacion__icontains=id_evaluacion)
        fecha_evaluaciones = Evaluacion.objects.filter(id_evaluacion__icontains=id_evaluacion)
        return render(request,"appproyecto3pe/buscarevaluacion.html", {"id_evaluadores":id_evaluadores,"id_asesores":id_asesores,"id_evaluacion":id_evaluacion,"fecha_evaluaciones":fecha_evaluaciones})
    else:
        return render(request,"appproyecto3pe/buscarevaluacionno.html")
    
