"""iteduca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from courses.views import index, lista_cursos, ListaCursosView, registrar_curso
from estudiantes.views import registrar_estudiante, editar_estudiante, lista_estudiantes, eliminar_estudiante, \
    ListaEstudiantesView, NuevoEstudiantesView, DetalleEstudianteView, detalle_estudiante
from accounts.views import login_view, logout_view, change_password

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='inicio'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^cambiar/contrasena/$', change_password, name='change_password'),

    # cursos
    url(r'^cursos/$', lista_cursos, name='lista_cursos'),
    url(r'^cursos/nuveo/$', registrar_curso, name='registrar_curso'),

    # URLs para vistas basadas en funcion
    url(r'^lista/cursos/$', ListaCursosView.as_view(), name='list_courses'),


    # estudiantes
    # URLs para vistas basadas en funcion
    url(r'^estudiantes/$', lista_estudiantes, name='lista_estudiantes'),
    url(r'^estudiantes/nuevo/$', registrar_estudiante, name='registrar_estudiante'),
    url(r'^estudiantes/editar/(?P<pk>\d+)/$', editar_estudiante, name='editar_estudiante'),
    url(r'^estudiantes/eliminar/(?P<pk>\d+)/$', eliminar_estudiante, name='eliminar_estudiante'),
    url(r'^estudiantes/detalle/(?P<pk>\d+)/$', detalle_estudiante, name='detalle_estudiante'),

    # URLs para vistas basadas en clases para su revision colocar el patron de url que hace llamado a la otra forma
    # de declarar vistas
    url(r'^lista/estudiantes/$', ListaEstudiantesView.as_view(), name='list_student'),
    url(r'^nuevo/estudiantes/$', NuevoEstudiantesView.as_view(), name='create_student'),
    url(r'^ver/estudiantes/(?P<pk>\d+)/$', DetalleEstudianteView.as_view(), name='view_student'),
    url(r'^editar/estudiantes/(?P<pk>\d+)/$', editar_estudiante, name='edit_student'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)