from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """"""
    # logica de la vista
    mensaje = "Iniciando el manejo de vistas en django"
    ctx = {"mensaje": mensaje}

    return render(request, "inicio.html", context=ctx)