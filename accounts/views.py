from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm


def login_view(request):
    form = LoginForm()  # incializar el formulario de Login

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():  # si el formulario cumple con la validacion
            # retorna un diccionario con los valores del form
            cd = form.cleaned_data
            user = authenticate(username=cd['usuario'], password=cd['clave'])
            if user is not None:
                login(request, user)
                messages.success(request, "Bienvenidos a su sisteam ITEDU")
                return render(request, 'inicio.html', {'user': user})
            else:
                messages.error(request, "El usuario no se encuentra en el sisteam ITEDU")
                return render(request, 'login.html', context={
                    'form': form,
                })
        else:
            messages.error(request, "Error: Las credenciales no cumplen "
                                    "con el formato")
            return render(request, 'login.html', context={
                'form': form,
            })
    return render(request, 'login.html', context={
        'form': form,
    })


def logout_view(request):
    logout(request)
    return redirect('login')