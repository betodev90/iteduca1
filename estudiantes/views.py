from django.shortcuts import render, redirect
from .forms import FormEstudiante
from django.contrib import messages
from estudiantes.models import Estudiante
# Create your views here.


def registrar_estudiante(request):
    form = FormEstudiante()
    if request.method == 'POST':
        form = FormEstudiante(request.POST)
        print("Errores: ", form.errors)
        if form.is_valid():
            print('Ingreso')
            data = form.cleaned_data
            print(data.get('sexo'))
            Estudiante.objects.create(email=data.get('email'), nombres=data.get('nombres'),
                                      apellidos=data.get('apellidos'), username=data.get('usuario'),
                                      password=data.get('contrasenia'), fecha_nacimiento=data.get("fecha_nac"),
                                      sexo=data.get('sexo')
                                      )
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