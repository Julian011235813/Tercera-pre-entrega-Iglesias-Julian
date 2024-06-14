from django.urls import path
from appdeinicio import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('profesor/', views.profesor, name='profesor'),
    path('profes_lista/', views.lista_profe, name='lista_profe'),
    path('alumno/', views.alumno, name='alumno'),
    path('alumno_lista/', views.lista_alumno, name='lista_alumno'),
    path('prueba/', views.prueba, name='prueba'),
    path('prueba_lista/', views.lista_prueba, name='lista_prueba')    
]	
  