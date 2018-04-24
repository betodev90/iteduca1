from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

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


@login_required(login_url='/login')
def registrar_curso(request):
    return render(request, 'create_cursos.html', context={})


# Vistas Basadas en Clase (VCB)

class ListaCursosView(LoginRequiredMixin, ListView):
    """Vista Basda en Clase, controlador de Django para listar objetos de la clase Curso
        NOTA: Realiza el mismo proceso que la vista 'lista_cursos'
    """
    model = Curso
    # Redirect al login si al intentar acceder a esta vista no esta ha hecho login
    login_url = reverse_lazy('login')
    # Template a utilizar para renderizar
    template_name = 'list_cursos.html'
    # Le indica que nombre lo va a llamar desde el template si no asignamos el atributo 'context_object_name' asume
    # que en el template tiene que estar la variable {{ object_list }}
    context_object_name = 'cursos'
    # Query consulta filtrado
    queryset = Curso.objects.all()
    # Indica cuando se quiere aplicar paginacion
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        querys = (Q(titulo__icontains=q) | Q(asignatura__titulo__icontains=q))
        object_list = Curso.objects.filter(querys)
        return object_list