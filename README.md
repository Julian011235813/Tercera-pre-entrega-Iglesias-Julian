# README del ejercicio 3

### Descripción del proyecto

Este proyecto es un ejercicio de Python con Django que incluye funcionalidades para gestionar los objetos Alumnos, Profesores y Pruebas.
El proyecto permite crear y visualizar alumnos, profesores y pruebas utilizando formularios y vistas.


1. Página de Inicio
URL: /
Descripción: Muestra la página de inicio de la aplicación.
2. Crear Alumno
URL: /alumno/
Descripción: Permite crear un nuevo alumno utilizando un formulario.
3. Listar Alumnos
URL: /alumnos/
Descripción: Muestra una lista de todos los alumnos registrados.
4. Listar Prueba
URL: /prueba/
Descripción: Muestra una lista de todos los alumnos registrados.

5. Estructura del Proyecto
appdeinicio: Carpeta que contiene la aplicación. Dentro

models.py: Define los modelos de la base de datos (Alumno, Profe, Pruebas).
Los modelos sirven para estructurar y gestionar los datos en la base de datos de forma sencilla y eficiente.
Son clases que crean los objetos y sus atributos con los que se va a trabajar en la programacion.

views.py: Contiene las funciones que manejan las peticiones HTTP que llegan a la aplicación (inicio, profesor, lista_profesor, etc).
A partir de estas funciones, se generan las funcionalidades en la app.

forms.py: Define los formularios que se utilizan para recolectar y validar datos ingresados por los usuarios en la aplicación (CrearProfeForm, CrearAlumnoForm, CrearPruebaForm).
Es el espacio donde se indican los inputs que tendra la app para interactuar con el usuario.

urls.py: Define las rutas de las vistas. Existen dos urls.py:

  urls.py en el directorio principal del proyecto: Este archivo de URLs se encuentra en el directorio raíz del proyecto y se utiliza para definir las rutas principales de la aplicación. Aquí es donde se incluyen las URLS que apuntan a diferentes aplicaciones dentro del proyecto.

  urls.py en el directorio de la aplicación: Cada aplicación Django puede tener su propio archivo urls.py dentro de su directorio. Este archivo se utiliza para definir las rutas específicas de esa aplicación. Es decir, las URLs que están relacionadas directamente con las vistas y funcionalidades de esa aplicación en particular.
