from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    hijos=models.IntegerField()
    
    

class Direccion(models.Model):
    ubicacion: models.CharField(max_length=100)