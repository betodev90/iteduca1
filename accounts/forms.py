from django import forms # importamos el core de django forms


class LoginForm(forms.Form):
    """Formulario para login"""
    usuario = forms.CharField(max_length=10)
    clave = forms.CharField(widget=forms.PasswordInput, max_length=15, min_length=4)

    # Especificar clases a los controles o elementos del form
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs['class'] = 'form-control input-lg'
        self.fields['usuario'].widget.attrs['placeholder'] = 'Ingrese su usuario'
        self.fields['clave'].widget.attrs['class'] = 'form-control input-lg'
        self.fields['clave'].widget.attrs['placeholder'] = 'Ingrese su contraseña'
