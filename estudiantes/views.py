from django.shortcuts import render, redirect
from .forms import FormEstudiante
from django.contrib import messages
from estudiantes.models import Estudiante
# Create your views here.


def registrar_estudiante(request):
    form = FormEstudiante()
    if request.method == 'POST':
        form = FormEstudiante(request.POST, request.FILES)
        print("Errores: ", form.errors)
        if form.is_valid():
            print('Ingreso')
            data = form.cleaned_data
            Estudiante.objects.create(
                email=data.get('email'), nombres=data.get('nombres'),
                apellidos=data.get('apellidos'), username=data.get('usuario'),
                password=data.get('contrasenia'), fecha_nacimiento=data.get("fecha_nac"),
            )
            # estudiante = Estudiante()
            # estudiante.nombres = data.get('nombres')
            # estudiante.apellidos = data.get('apellidos')
            # estudiante.username = data.get('usuario')
            # estudiante.password = data.get('contrasenia')
            # print(data.get('fecha_nac'))
            # estudiante.fecha_nacimiento = data.get("fecha_nac")
            # estudiante.save()
            messages.success(request, "Se ha creado exitosamente un estudiante")
            return redirect('inicio')

        else:
            lista_errores = "Por favor verifique los siguientes campos: "
            for i in form.errors:
                lista_errores = lista_errores + i + ", "
            if form.errors:
                messages.error(request, lista_errores[0:-2])
            for i in form:
                if i.errors:
                    i.field.widget.attrs['class'] = 'danger'

    return render(request, 'form.html', {'form': form})


def editar_estudiante(request, pk):
    """Editar estudiante"""

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


def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', context={'estudiantes': estudiantes})