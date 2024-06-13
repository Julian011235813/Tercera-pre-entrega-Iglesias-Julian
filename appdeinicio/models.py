from django.db import models

# Create your models here.

class Auto(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    color = models.CharField(max_length=50)
    patente = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.marca} {self.modelo} {self.anio} {self.color} {self.patente}"
