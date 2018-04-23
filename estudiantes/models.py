from django.contrib.auth.models import User
from django.db import models


def url(self, filename):
    ruta = str("usuarios/%s" % filename)
    return ruta


class Estudiante(User):
    SEXO_OPCIONES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    ESTADOS_OPCIONES = (
        (0, 'Pendiente'),
        (1, 'Activo'),
        (2, 'Inactivado'),
        (3, 'Eliminado'),
        (4, 'Aprobado'),
        (5, 'Reprobado'),
    )
    nombres = models.CharField(max_length=250, verbose_name="Nombres")
    apellidos = models.CharField(max_length=250)
    # No olvidar instalar la dependencia de imagenes / Pillow, puede ser null en la BD
    foto = models.ImageField(upload_to=url, verbose_name="Foto", null=True)
    fecha_nacimiento = models.DateField()
    # Puede se null en la bd y no requerido en el admin de django
    sexo = models.CharField(choices=SEXO_OPCIONES, max_length=5, null=True, blank=True)
    facebook = models.CharField(
        max_length=220, null=True, blank=True,
        help_text='Ingrese el nombre de su cuenta en fb'
    )
    # Puede se null en la bd y no requerido en el admin de django
    direccion = models.CharField(max_length=220, null=True, blank=True)
    # Puede se null en la bd y no requerido en el admin de django
    telefono = models.CharField(max_length=220, null=True, blank=True)

    # Informacion de auditoria
    estado = models.PositiveIntegerField(choices=ESTADOS_OPCIONES, default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.CharField(max_length=50)
    usuario_actualizacion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        # Ejemplo de como django lee una tabla ya creada en una base de datos existente usando en el Meta 'db_table'
        # db_table = "persona"

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)