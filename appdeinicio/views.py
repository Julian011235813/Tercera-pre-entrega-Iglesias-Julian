from django.shortcuts import render, redirect
from appdeinicio.forms import CrearAlumnoForm, CrearProfesorForm, CrearPruebaForm

import random

from appdeinicio.models import Alumno, Profe, Prueba


def inicio(request):
   #return HttpResponse("Estás en la página de inicio de la aplicación Ejercicio3.")
  return render(request, 'appdeinicio/index.html')


def profesor(request):
  formulario = CrearProfesorForm()  
  if request.method == 'POST':
    formulario = CrearProfesorForm(request.POST)
    if formulario.is_valid():
      datos = formulario.cleaned_data
      profe = Profe(nombre=datos.get('nombre'), apellido=datos.get('apellido'))
      profe.save()
      return redirect('lista_profe')     
  return render(request, 'appdeinicio/profesor.html', {'formulario': formulario})

def lista_profe(request):  
  profes = Profe.objects.all()  
  return render(request, 'appdeinicio/lista_profes.html', {'profes': profes})
  

def alumno(request):
  formulario = CrearAlumnoForm()  
  if request.method == 'POST':
    formulario = CrearAlumnoForm(request.POST)
    if formulario.is_valid():
      datos = formulario.cleaned_data
      alumno = Alumno(nombre=datos.get('nombre'), apellido=datos.get('apellido'), nota=datos.get('nota'))
      alumno.save()
      return redirect('lista_alumno')     
  return render(request, 'appdeinicio/alumno.html', {'formulario': formulario})  

def lista_alumno(request):  
  alumnos = Alumno.objects.all()  
  return render(request, 'appdeinicio/lista_alumnos.html', {'alumnos': alumnos})


def prueba(request):
  formulario = CrearPruebaForm()
  if request.method == 'POST':
    formulario = CrearPruebaForm(request.POST)
    if formulario.is_valid():
      datos = formulario.cleaned_data
      prueba = Prueba(materia=datos.get('materia'), dificultad=datos.get('dificultad'))
      prueba.save()
      return redirect('lista_prueba')     
  return render(request, 'appdeinicio/prueba.html', {'formulario': formulario})  

def lista_prueba(request):
  pruebas = Prueba.objects.all()  
  return render(request, 'appdeinicio/lista_pruebas.html', {'pruebas': pruebas})