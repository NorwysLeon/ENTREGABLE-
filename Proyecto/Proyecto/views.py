from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

def inicio(request):
    return HttpResponse("Hola.! Bienvenid@")

def familiares(request):
    return HttpResponse("Datos de familiares")

def saludo_con_nombre(request, nombre):
    return HttpResponse(f"Hola {nombre} como estas")

def mostrando_familiares(request):
    
    familiar1={"nombre":"Luigi", "apellido":"Marsili", "edad":"33", "fecha": datetime.datetime.today()}
    familiar2={"nombre":"Mateo", "apellido":"Marsili", "edad":"2", "fecha": datetime.datetime.today()}
    familiar3={"nombre":"Norwys", "apellido":"Leon", "edad":"32", "fecha": datetime.datetime.today()}

    """archivo=open("C:/Users/norwy/Mi unidad/CursoPython Coder House/Clase_18/MTV NORWYS LEON/Proyecto/Plantillas/template1.html")
    
    template=Template(archivo.read())
    archivo.close()
    contexto=Context(diccionario)"""

    template=loader.get_template("template1.html")

    documento=template.render({"familiares": [familiar1, familiar2, familiar3]})
    return HttpResponse(documento)


