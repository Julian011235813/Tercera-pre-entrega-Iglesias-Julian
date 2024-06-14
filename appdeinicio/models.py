from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nota = models.IntegerField()
    def __str__(self):
        return f"El alumno {self.nombre} {self.apellido} sacó un {self.nota}"


class Profe(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    def __str__(self):
        return f"El profesor {self.nombre} {self.apellido} tomó la clase de Python."
    
    
class Prueba(models.Model):
    materia = models.CharField(max_length=50)
    dificultad = models.CharField(max_length=50)
    def __str__(self):
        return f"La prueba de la materia {self.materia} es de dificultad {self.dificultad}"