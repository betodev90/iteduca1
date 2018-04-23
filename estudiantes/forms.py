from django import forms
from django.contrib.auth.models import User
import datetime


class EstudiantesModelForm(forms.ModelForm):
    """"""


class FormEstudiante(forms.Form):
    SEXO_OPCIONES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    nombres = forms.CharField(max_length=100, label=u"Nombres")
    apellidos = forms.CharField(max_length=100, label=u"Apellidos")
    usuario = forms.CharField(min_length=4, max_length=20, label=u"Usuario")
    contrasenia = forms.CharField(widget=forms.PasswordInput(), label=u"Clave", max_length=24)
    comfirma_contrasenia = forms.CharField(widget=forms.PasswordInput(), label="Confirmar Clave", max_length=24)
    fecha_nac = forms.DateField(label=u"Fecha Nacimiento", widget=forms.DateInput(format=("%Y-%m-%d")))
    telefono = forms.CharField(label=u"Teléfono", max_length=12, required=False)
    direccion = forms.CharField(label=u"Dirección", required=False)
    email = forms.EmailField(label=u"Email")
    estado_civil = forms.ChoiceField(choices='', widget=forms.RadioSelect(),
                                     label=u"Estado Cívil", required=False)
    sexo = forms.ChoiceField(choices=SEXO_OPCIONES)
    foto = forms.ImageField(required=False, label=u"Foto")
    facebook = forms.CharField(required=False, max_length=100, label="Facebook")

    # para agregar propiedades a los atributos de la clase FormEstudiante
    def __init__(self, *args, **kwargs):
        super(FormEstudiante, self).__init__(*args, **kwargs)
        self.fields['fecha_nac'].widget.attrs['data-date-format'] = "yyyy-mm-dd"
        self.fields['fecha_nac'].widget.attrs['placeholder'] = "0000-00-00"
        self.fields['email'].widget.attrs['placeholder'] = "email@ejemplo.com"
        self.fields['telefono'].widget.attrs['placeholder'] = "(99) 9999-9999"

    # Validaciones del formulario
    def clean_contrasenia(self):
        password1 = self.cleaned_data.get('contrasenia')
        password2 = self.cleaned_data.get('comfirma_contrasenia')

        if password1 is not None:
            if len(password1) < 5:
                raise forms.ValidationError("Error: la contraseña ingresada debe ser mayor a 5 carácteres")

        elif password1 != password2:
            raise forms.ValidationError("Error: lContraseñas diferentes")

        return password1

    def clean_fecha_nac(self):
        fecha_nac = self.cleaned_data.get('fecha_nac')
        if fecha_nac != "" and fecha_nac is not None:
            if fecha_nac.year > (datetime.datetime.now().year - 18):
                raise forms.ValidationError("El usuario debe ser mayor de 18 años")
        return fecha_nac

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Error: El email ya esta asignado a otro usuario")
        return email

    def clean_usuario(self):
        usuario = self.cleaned_data.get('usuario')
        if User.objects.filter(username=usuario).exists():
            msg = "El usuario ya ha sido ingresado"
            raise forms.ValidationError(msg)
        return usuario

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')
        if apellidos:
            cont = 0
            letras = str(apellidos).split(" ")
            for i in letras:
                if not i.isalpha():
                    cont += 1
            if cont == 0:
                return apellidos
            else:
                raise forms.ValidationError("Ingrese correctamente la informacion de apellidos")