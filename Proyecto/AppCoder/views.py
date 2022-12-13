from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse



def familia(request):
    familiares1=Familia(nombre="Norwys", apellido="Leon", hijos=1)
    familiares1.save()
    cadena_texto=f"Miembro de la familia: {familiares1.nombre} {familiares1.apellido} y tiene {familiares1.hijos} hijos"
    return HttpResponse(cadena_texto)
