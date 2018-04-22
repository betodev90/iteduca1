from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login')
def index(request):
    """"""
    # logica de la vista
    mensaje = "Iniciando el manejo de vistas en django"
    ctx = {"mensaje": mensaje}

    return render(request, "inicio.html", context=ctx)