from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

import random

from appdeinicio.models import Auto

def inicio(request):
   #return HttpResponse("Hola, mundo. Estás en la página de inicio de la aplicación Ejercicio3.")
  return render(request, 'appdeinicio/index.html')

def template1(request, nombre, apellido):
  fecha = datetime.now()
  return HttpResponse(f"<h1>Este es el template 1</h1> -- Fecha: {fecha} -- Nombre: {nombre}, Apellido: {apellido}")

def template2(request, nombre, apellido):
  archivotemplateabierto = open(r"C:\Users\julia\OneDrive\Documents\Coderhouse\RepositorioEjercicio3\templates\template2.html")
  template = Template(archivotemplateabierto.read())
  archivotemplateabierto.close()
  datosparacontexto = {"nombre": nombre,
                       "apellido": apellido}  
  contexto = Context(datosparacontexto)
  template_renderizado = template.render(contexto)
  return HttpResponse(template_renderizado)

def template3(request, nombre, apellido):
  #archivotemplateabierto = open(r"C:\Users\julia\OneDrive\Documents\Coderhouse\RepositorioEjercicio3\templates\template2.html")
  #template = Template(archivotemplateabierto.read())
  #archivotemplateabierto.close()
  fecha = datetime.now()
  template =  loader.get_template('template3.html')
  datosparacontexto = {"nombre": nombre,
                       "apellido": apellido,
                       "fecha": fecha}  
  #contexto = Context(datosparacontexto)
  template_renderizado = template.render(datosparacontexto)
  return HttpResponse(template_renderizado)

def template4(request, nombre, apellido):
  fecha = datetime.now()
  datosparacontexto = {"nombre": nombre,
                       "apellido": apellido,
                       "fecha": fecha}
  return render(request, 'template4.html', datosparacontexto)

def probando(request):
  lista = list(range(500))
  numeros=random.choices(lista, k=50)
  print(numeros)
  return render(request, 'probando_if_for.html', {"numeros": numeros})

def crear_auto(request, marca, modelo, anio):
  auto = Auto(marca=marca, modelo=modelo, anio=anio)
  auto.save()
  return render(request, 'otracarpetadetemplates/templateauto.html', {"auto": auto})