from django.http import HttpResponse

def inicio(request):
   return HttpResponse("Hola, mundo. Estás en la página de inicio de la aplicación Ejercicio3.")
 