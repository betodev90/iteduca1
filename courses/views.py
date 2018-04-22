from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    q = request.GET.get('q', '')
    querys = (Q(titulo__icontains=q) | Q(asignatura__titulo__icontains=q))
    cursos = Curso.objects.filter(querys)
    page = request.GET.get('page', 1)
    paginator = Paginator(cursos, 5)
    try:
        cursos = paginator.page(page)
    except PageNotAnInteger:
        cursos = paginator.page(1)
    except EmptyPage:
        cursos = paginator.page(paginator.num_pages)
    return render(request, 'list_cursos.html', context={'cursos': cursos})