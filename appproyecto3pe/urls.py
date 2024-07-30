from django.contrib import admin
from django.urls import path
from appproyecto3pe.views import *
from appproyecto3pe import views

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('asesores/', asesores, name = "asesores"),
    path('evaluadores/', evaluadores, name = "evaluadores"),
    path('evaluaciones/', evaluaciones, name = "evaluaciones"),
]

form_asesor = [
    path('asesorformulario/',views.asesor_formulario, name="AsesorFormulario"),
    path('asesorregistrado/',views.asesorregistrado, name="AsesorRegistrado"),
    path('busquedaasesor', views.busquedaasesor, name="BusquedaAsesor"),
    path('buscaras/', views.buscar_as, name="BuscarAsesor"),
]

urlpatterns += form_asesor

form_evaluador = [
    path('evaluadorformulario/',views.evaluador_formulario, name="EvaluadorFormulario"),
    path('evaluadorregistrado/',views.evaluadorregistrado, name="EvaluadorRegistrado"),
    path('busquedaevaluador', views.busquedaevaluador, name="BusquedaEvaluador"),
    path('buscarevdor/', views.buscar_evdor, name="BuscarEvaluador"),
]

urlpatterns += form_evaluador

form_evaluacion = [
    path('evaluacionformulario/',views.evaluacion_formulario, name="EvaluacionFormulario"),
    path('evaluacionregistrada/',views.evaluacionregistrada, name="EvaluacionRegistrada"),
    path('busquedaevaluacion', views.busquedaevaluacion, name="BusquedaEvaluacion"),
    path('buscarevalu/', views.buscar_evalu, name="BuscarEvaluacion"),
    
]

urlpatterns += form_evaluacion