from django.contrib import admin
from courses.models import Asignatura, Curso

# Register your models here.


@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    fields = ('titulo', 'estado', 'descripcion')
    list_filter = ('estado',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    fields = ('titulo', 'slug', 'asignatura', 'propietario', 'descripcion')
    prepopulated_fields = {'slug': ('titulo',)}
    search_fields = ('titulo',)
    list_filter = ('asignatura',)