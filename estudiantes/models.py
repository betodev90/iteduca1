from django.contrib.auth.models import User
from django.db import models

# Create your models here.


def url(self, filename):
    ruta = str("usuarios/%s" % filename)
    return ruta


class Estudiante(User):
    SEXO_OPCIONES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    ESTADO_CIVIL_OPCIONES = (
        ('s', 'Soltero(a)'),
        ('c', 'Casado(a)'),
        ('u', 'Union'),
        ('d', 'Divorsiad(a)'),
        ('v', 'Viudo(a)'),
    )
    ESTADOS_OPCIONES = (
        (0, u'Pendiente'),
        (1, u'Activo'),
        (2, u'Inactivado'),
        (3, u'Eliminado'),
    )

    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    sexo    = models.CharField(max_length=220, choices=SEXO_OPCIONES)
    # No olvidar instalar la dependencia de imagenes / Pillow
    foto    = models.ImageField(upload_to=url, verbose_name="Imagen", null=True)
    estado_civil = models.CharField(max_length=220, null=True, choices=ESTADO_CIVIL_OPCIONES)
    fecha_nacimiento    = models.DateField(auto_now_add=True)
    facebook            = models.CharField(max_length=220, null=True, blank=True)
    direccion           = models.CharField(max_length=220, null=True, blank=True)
    telefono            = models.CharField(max_length=220, null=True, blank=True)
    es_admin            = models.BooleanField(default=False)

    estado              = models.PositiveIntegerField(choices=ESTADOS_OPCIONES, default=1)
    fecha_creacion  =   models.DateTimeField(auto_now_add=True)
    fecha_actualizacion  =   models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=50)
    usuario_actualizacion = models.CharField(max_length=50)

    # class Meta:
    #     db_table = "persona"

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)