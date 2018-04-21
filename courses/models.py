from django.db import models
# Importamos la tabla del core de Django 'User'
from django.contrib.auth.models import User

# Create your models here.


class Asignatura(models.Model):
    # propiedades o atributos
    titulo = models.CharField(
        verbose_name='Título', max_length=250,
    )
    descripcion = models.TextField(default="Inicio de descripcion: ")

    estado = models.BooleanField(verbose_name='Estado')
    fecha_creacion = models.DateTimeField(
        verbose_name="Fecha de creacion", auto_now_add=True)
    fecha_modificacion = models.DateTimeField(
        verbose_name="Fecha de modificacion", auto_now=True
    )

    def __str__(self):
        return self.titulo


class Curso(models.Model):
    propietario = models.ForeignKey(
        User, related_name='propietario_curso'
    )
    asignatura = models.ForeignKey(
        Asignatura, related_name='asignatura_curso'
    )
    descripcion = models.TextField(default='')
    titulo = models.CharField(max_length=220)
    slug = models.SlugField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'



