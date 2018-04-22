from django import forms # importamos el core de django forms


class LoginForm(forms.Form):
    """Formulario para login"""
    usuario = forms.CharField(max_length=10)
    clave = forms.CharField(widget=forms.PasswordInput, max_length=15, min_length=4)
    next = forms.CharField(min_length=3, max_length=100, required=False)

    # Especificar clases a los controles o elementos del form
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs['class'] = 'form-control input-lg'
        self.fields['usuario'].widget.attrs['placeholder'] = 'Ingrese su usuario'
        self.fields['clave'].widget.attrs['class'] = 'form-control input-lg'
        self.fields['clave'].widget.attrs['placeholder'] = 'Ingrese su contraseña'
        self.fields['next'].label = ""
        self.fields['next'].widget.attrs['style'] = "display: none"
