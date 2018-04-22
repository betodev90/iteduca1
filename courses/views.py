from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Curso


@login_required(login_url='/login')
def index(request):
    """"""
    # logica de la vista
    mensaje = "Iniciando el manejo de vistas en django"
    ctx = {"mensaje": mensaje}
    return render(request, "inicio.html", context=ctx)


@login_required(login_url='/login')
def lista_cursos(request):
    """"""
    cursos = Curso.objects.all()
    return render(request, 'list_cursos.html', context={'cursos': cursos})