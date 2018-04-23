from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from .forms import LoginForm


def login_view(request):
    """"""
    if not request.user.is_authenticated():
        siguiente = request.GET.get("next", "")
        form = LoginForm(initial={"siguiente": siguiente})  # incializar el formulario de Login
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():  # si el formulario cumple con la validacion
                # retorna un diccionario con los valores del form
                cd = form.cleaned_data
                siguiente = form.cleaned_data["next"]
                user = authenticate(username=cd['usuario'], password=cd['clave'])
                if user is not None:
                    login(request, user)
                    messages.success(request, "Bienvenidos a su sisteam ITEDU")
                    if siguiente != "":
                        return redirect(siguiente)
                    else:
                        return redirect(reverse("inicio"))
                    # return render(request, 'inicio.html', {'user': user})
                else:
                    messages.error(request, "El usuario no se encuentra en el sisteam ITEDU")
                    return render(request, 'login.html', context={
                        'form': form,
                    })
            else:
                form = LoginForm(initial={"siguiente": siguiente})
                messages.error(request, "Error: Las credenciales no cumplen con el formato")
                return render(request, 'login.html', context={
                    'form': form,
                })
        else:
            form = LoginForm(initial={"siguiente": siguiente})
            return render(request, 'login.html', context={
                'form': form
            })
    else:
        return redirect(reverse("inicio"))


def logout_view(request):
    logout(request)
    return redirect('login')


def change_password(request):
    """Vista basada en funcion para cambiar contraseña de un usuario"""
    if request.method == 'POST':
        # Declara formulario del core de django para cambiar contrasenia
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Actualiza directamente la informacion del usuario debido a que el PasswordChangeForm mapea
            # el model User de django
            user = form.save()
            # Llama al metodo que setea la sesion IMPORTANTE
            update_session_auth_hash(request, user)
            messages.success(request, 'Su contraseña ha sido actualizado exitoósamente!')
            return redirect('login')
        else:
            messages.error(request, 'Favor corrija la información del formulario')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })