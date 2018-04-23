from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib import messages

from .forms import FormEstudiante
from estudiantes.models import Estudiante

# Apartado de VBF ( Vista Basadas en Función )


@login_required(login_url='/login')
def registrar_estudiante(request):
    """Vista vasada en funcion para crear un nuevo objeto Estudiante"""
    form = FormEstudiante()  # Declaracion del formulario
    if request.method == 'POST':
        form = FormEstudiante(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Estudiante.objects.create(
                email=data.get('email'), nombres=data.get('nombres'),
                apellidos=data.get('apellidos'), username=data.get('usuario'),
                password=data.get('contrasenia'), fecha_nacimiento=data.get("fecha_nac"), sexo=data.get('sexo')
            )
            # Nueva Alternativa para crear un nuevo objeto Estudiante
            # estudiante = Estudiante()
            # estudiante.nombres = data.get('nombres')
            # estudiante.apellidos = data.get('apellidos')
            # estudiante.username = data.get('usuario')
            # estudiante.password = data.get('contrasenia')
            # print(data.get('fecha_nac'))
            # estudiante.fecha_nacimiento = data.get("fecha_nac")
            # estudiante.save()
            messages.success(request, "Se ha creado exitosamente un estudiante")
            return redirect('lista_estudiantes')
        else:
            # Forma para acceder a los mensajes de error que generamos en el clean_data (validacion de formularios)
            lista_errores = "Por favor verifique los siguientes campos: "
            for i in form.errors:
                lista_errores = lista_errores + i + ", "
            if form.errors:
                messages.error(request, lista_errores[0:-2])
            for i in form:
                if i.errors:
                    i.field.widget.attrs['class'] = 'danger'
    return render(request, 'form.html', {'form': form})


@login_required(login_url='/login')
def editar_estudiante(request, pk):
    """Vista Basada en Funcion para Editar la informacion de un objeto estudiante"""

    estudiante = Estudiante.objects.get(pk=pk)

    form = FormEstudiante(initial={
        'nombres': estudiante.nombres,
        'apellidos': estudiante.apellidos,
        'fecha_nac': estudiante.fecha_nacimiento,
        'email': estudiante.email,
    })

    if request.method == 'POST':
        form = FormEstudiante(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            estudiante.nombres = data.get('nombres')
            estudiante.apellidos = data.get('apellidos')
            estudiante.save()

            messages.success(request, "Se realizo el cambio exitosamente")
            return redirect("inicio")
        else:
            messages.error(request, "")
    return render(request, 'form.html', {'form': form})


@login_required(login_url='/login')
def eliminar_estudiante(request, pk):
    """Cambia de estado al estudiante se le envia por parametro el pk (identificador único de un objeto)"""
    try:
        # Obtiene el objeto Estudiante haciendo la consulta mediante el metodo get(pk=pk)
        estudiante = Estudiante.objects.get(pk=pk)
        if request.method == 'POST':
            if estudiante.estado == 1:  # estudiante activo
                estudiante.estado = 2   # estudiante estado 'inactivo'
                estudiante.save(update_fields=['estado'])   # le indica a Django que solo actualiza ese campo 'estado'
                # mensaje enviado al template para retroalimentar al usuario
                messages.success(request, "Se realizo el cambio exitosamente")

                # imporante la vista debe retornar un HttResponse en este caso llamamos al método
                # redirect('') de django, el parametro que se le envia al
                # redirect( < el tercer parametro de la url declarado en el fichero urls.py en este caso
                # name='lista_estudiantes' >)
                return redirect("lista_estudiantes")
            else:
                messages.info(request, "El estudiante ya se encuentra eliminado")
        return redirect('lista_estudiantes')
    except Estudiante.DoesNotExist:  # Manejo de Excepcion si no encuentra el objecto, similar al Try catch de Java
        # Si ingresa a este bloque es porque accedió a la excepcion, es decir no encontró al objecto Estudiante con ese
        # pk enviando en la vista.
        messages.error(
            request, "El estudiante seleccionado no se encuentra en el sistema, favor verifique con el admin"
        )
        return redirect('lista_estudiantes')


@login_required(login_url='/login')
def lista_estudiantes(request):
    """"""
    q = request.GET.get('q', '')
    querys = (Q(nombres__icontains=q) | Q(apellidos__icontains=q) | Q(email__exact=q))
    estudiantes = Estudiante.objects.filter(estado=1).filter(querys)   # estudiantes activos
    page = request.GET.get('page', 1)
    paginator = Paginator(estudiantes, 10)
    try:
        estudiantes = paginator.page(page)
    except PageNotAnInteger:
        estudiantes = paginator.page(1)
    except EmptyPage:
        estudiantes = paginator.page(paginator.num_pages)
    return render(request, 'lista_estudiantes.html', context={'estudiantes': estudiantes})

# Apartado de VBC ( Vista Basadas en clase )


class ListaEstudiantesView(ListView):
    """Vista Basda en Clase , controlador de Django para listar objetos de la clase Estudiante
        NOTA: Realiza el mismo proceso que la vista 'lista_estudiantes'
    """
    model = Estudiante
    # Template a utilizar para renderizar
    template_name = 'lista_estudiantes.html'
    # Le indica que nombre lo va a llamar desde el template si no asignamos el atributo 'context_object_name' asume
    # que en el template tiene que estar la variable {{ object_list }}
    context_object_name = 'estudiantes'
    # Query consulta filtrado
    queryset = Estudiante.objects.filter(estado=1)  # estudiantes activos
    # Indica cuando se quiere aplicar paginacion
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        # parametros de filtro | busqueda
        querys = (Q(nombres__icontains=q) | Q(apellidos__icontains=q) | Q(email__exact=q))
        object_list = Estudiante.objects.filter(querys)
        return object_list


class NuevoEstudiantesView(CreateView):
    """Vista Basda en Clase , controlador de Django para crear un nuevo objeto estudiante"""
    # Model del objeto que va a crear la vista
    model = Estudiante
    # Indica el template a renderizar
    template_name = 'form.html'
    # Mapea los campos del model Estudiantes y los crea como formulario IMPORTANTE en el template que utilizamos debe
    # nombrar el formulario en el HTML como "{{ form }} "
    fields = ['nombres', 'apellidos', 'fecha_nacimiento', 'username', 'password', 'email', 'facebook']
    # metodo reverse_lazy(<url_name>) para que redireccione una vez agregue el objeto estudiante
    success_url = reverse_lazy('lista_estudiantes')